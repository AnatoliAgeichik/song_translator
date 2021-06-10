from rest_framework import generics, permissions
from rest_framework.response import Response
from google_trans_new import google_translator
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter


from .models import Track, Singer, Translation, User, Comment
from .serializers import SingerSerializer, TrackSerializer, TranslateSerializer, CommentSerializer
from .service import PaginationSingers, PaginationTracks, PaginationTranslation
from .permisisions import IsOwnerOrReadOnly


class TrackList(generics.ListCreateAPIView):
    pagination_class = PaginationTracks
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('track_name', 'original_language', 'singer__name')


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, pk):
        queryset = Comment.objects.filter(track_id=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TranslationList(APIView):
    pagination_class = PaginationTranslation
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('language',)
    ordering_fields = ('language',)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request, pk):
        translations = Translation.objects.filter(track_id=pk)
        paginator = PaginationTranslation()
        return paginator.generate_response(self.filter_queryset(translations), TranslateSerializer, request)

    def post(self, request, pk):
        translation_data = JSONParser().parse(request)
        if translation_data["auto_translate"]:
            translator = google_translator()
            track = Track.objects.get(id=pk)
            track_serializer = TrackSerializer(track)
            translation_data["text"] = translator.translate(track_serializer.data['text'],
                                                            lang_tgt=translation_data["language"],
                                                            lang_src=track_serializer.data[
                                                                'original_language'])
        serializer = TranslateSerializer(data=translation_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requet, pk):
        count = Translation.objects.filter(track_id=pk).delete()
        return Response({'message': f'{count[0]} translations were deleted successfully!'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def translate_detail(request, pk, transl_id):
    try:
        translate = Translation.objects.filter(track_id=pk, id=transl_id).get()
    except Translation.DoesNotExist:
        return Response({'The translate does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TranslateSerializer(translate)
        data = serializer.data['text']
        return Response(data)

    elif request.method == 'PUT':
        translate_data = JSONParser().parse(request)
        translate_serializer = TranslateSerializer(translate, data=translate_data)
        if translate_serializer.is_valid():
            translate_serializer.save()
            return Response(translate_serializer.data)
        return Response(translate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        translate.delete()
        return Response('Translation was deleted successfully!', status=status.HTTP_204_NO_CONTENT)


class SingerList(generics.ListCreateAPIView):
    pagination_class = PaginationSingers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)


class SingerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if not all(['email' in data, 'password' in data]):
            return JsonResponse({'error': 'password or email fields are not filled'},
                                status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(**data)
        token = Token.objects.create(user=user)
        return JsonResponse({'token': str(token)}, status=status.HTTP_201_CREATED)
    return JsonResponse({'error': 'No data'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = authenticate(request, email=data['email'], password=data['password'])
        except KeyError:
            return JsonResponse({'error': 'Could not login. Email or password is absent!'})
        if user is None:
            return JsonResponse(
                {'error': 'Could not login. Incorrect email or password!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = Token.objects.get(user=user)
        except ObjectDoesNotExist:
            token = Token.objects.create(user=user)
        return JsonResponse(
            {'token': str(token)}, status=status.HTTP_200_OK)
    return Response({'error': 'No data'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
