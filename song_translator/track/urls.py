from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TrackList, TrackDetail, SingerList, SingerDetail, TrackTranslate, track_translate

lang = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ny', 'co', 'hr', 'cs', 'da', 'nl',
         'en', 'eo', 'et', 'tl',
         'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'iw', 'he', 'hi', 'hu', 'is', 'icelandic', 'ga',
         'irish', 'it'
     , 'kn', 'kk', 'la', 'lv', 'lt', 'pl', 'pt', 'ru', 'es', 'sv', 'tg', 'tr', 'tk', 'uk', 'uz']
lang_re = '|'.join(lang)
urlpatterns = [
    path('tracks/', TrackList.as_view()),
    path('tracks/<int:pk>/', TrackDetail.as_view()),
    re_path(r'^tracks/(?P<pk>\d+)/(?P<lang>'+lang_re+')/$', track_translate),
    path('singers/', SingerList.as_view()),
    path('singers/<int:pk>/', SingerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
