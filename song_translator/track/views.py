from rest_framework import generics, permissions
from rest_framework.response import Response
from google_trans_new import google_translator
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import Track, Singer, Translate
from .serializers import SingerSerializer, TrackSerializer, TranslateSerializer
from .permisisions import IsOwnerOrReadOnly


class TrackList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


@api_view(['GET', 'PUT', 'DELETE'])
def track_translate(request, pk, lang):
    try:
        translate = Translate.objects.filter(track_id=pk, language=lang)
        if not translate:
            translator = google_translator()
            track = Track.objects.get(id=pk)
            track_serializer = TrackSerializer(track)
            Translate.objects.create(track_id=track, language=lang,
                                     text=translator.translate(track_serializer.data['text'],
                                                               lang_tgt=lang,
                                                               lang_src=track_serializer.data[
                                                                   'original_language']))
            translate = Translate.objects.filter(track_id=pk, language=lang)
        translate = translate.get()
    except Translate.DoesNotExist:
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
        return Response('Tutorial was deleted successfully!', status=status.HTTP_204_NO_CONTENT)


class SingerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
