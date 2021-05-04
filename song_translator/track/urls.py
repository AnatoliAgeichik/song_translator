from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TrackList, TrackDetail, SingerList, SingerDetail


urlpatterns = [
    path('tracks/', TrackList.as_view()),
    path('tracks/<int:pk>/', TrackDetail.as_view()),
    path('singers/', SingerList.as_view()),
    path('singers/<int:pk>/', SingerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
