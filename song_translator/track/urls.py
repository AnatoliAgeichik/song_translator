from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import TrackViewSet, SingerViewSet


router = DefaultRouter()
router.register(r'tracks', TrackViewSet, basename='Track')
router.register(r'singer', SingerViewSet, basename='Singer')
urlpatterns = router.urls
