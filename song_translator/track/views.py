from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Track, Singer
from .serializers import SingerSerializer, TrackSerializer


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class SingerViewSet(viewsets.ModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()
