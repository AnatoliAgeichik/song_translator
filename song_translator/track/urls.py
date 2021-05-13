from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TrackList, TrackDetail, SingerList, SingerDetail, track_translate

lang = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'co',
        'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha',
        'iw', 'he', 'hi',  'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo',
        'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa',
        'pl','pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw',
        'sv', 'tg', 'ta', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
lang_re = '|'.join(lang)
urlpatterns = [
    path('tracks/', TrackList.as_view()),
    path('tracks/<int:pk>/', TrackDetail.as_view()),
    re_path(r'^tracks/(?P<pk>\d+)/(?P<lang>'+lang_re+')/$', track_translate),
    path('singers/', SingerList.as_view()),
    path('singers/<int:pk>/', SingerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
