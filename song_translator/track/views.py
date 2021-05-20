from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from google_trans_new import google_translator
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Track, Singer, Translation,User
from .serializers import SingerSerializer, TrackSerializer, TranslateSerializer, RegistrationSerializer, LoginSerializer\
                         ,UserSerializer
from .permisisions import IsOwnerOrReadOnly
from .renderers import UserJSONRenderer


class TrackList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


@api_view(['GET', 'POST', 'DELETE'])
def translation_list(request, pk):
    if request.method == 'GET':
        translations = Translation.objects.filter(track_id=pk)

        serializer = TranslateSerializer(translations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        translation_data = JSONParser().parse(request)
        print(translation_data["auto_translate"])
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

    elif request.method == 'DELETE':
        count = Translation.objects.filter(track_id=pk).delete()
        return Response({'message': '{} translations were deleted successfully!'.format(count[0])},
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = LoginSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})


        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
