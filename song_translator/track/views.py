from rest_framework import generics, permissions
from rest_framework.response import Response
from google_trans_new import google_translator

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


class TrackTranslate(generics.ListCreateAPIView):
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer

    def get(self, request, pk, lang):
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
        serializer = TranslateSerializer(translate.get())
        data = serializer.data['text']
        return Response(data)


class SingerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
