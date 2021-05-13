from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TrackList, TrackDetail, SingerList, SingerDetail, track_translate, translation_list
from .utils import lang_re


urlpatterns = [
    path('tracks/', TrackList.as_view()),
    path('tracks/<int:pk>/', TrackDetail.as_view()),
    path('tracks/<int:pk>/translations/', translation_list),
    re_path(r'^tracks/(?P<pk>\d+)/translations/(?P<lang>'+lang_re+')/$', track_translate),
    path('singers/', SingerList.as_view()),
    path('singers/<int:pk>/', SingerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
