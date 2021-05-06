from rest_framework import generics, permissions
from rest_framework.response import Response
from google_trans_new import google_translator

from .models import Track, Singer
from .serializers import SingerSerializer, TrackSerializer
from .permisisions import IsOwnerOrReadOnly


class TrackList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class TrackTranslate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    def get(self, request, pk, lang):
        translator = google_translator()
        return Response(translator.translate(self.get_object().text, lang_tgt=lang))


class SingerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
