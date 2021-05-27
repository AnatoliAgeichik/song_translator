from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TrackList, TrackDetail, SingerList, SingerDetail, translate_detail, translation_list, \
    signup, sign_in


urlpatterns = [
    path('tracks/', TrackList.as_view()),
    path('tracks/<int:pk>/', TrackDetail.as_view()),
    path('tracks/<int:pk>/translations/', translation_list),
    path('tracks/<int:pk>/translations/<int:transl_id>/', translate_detail),
    path('singers/', SingerList.as_view()),
    path('singers/<int:pk>/', SingerDetail.as_view()),
    path('users/', signup),
    path('users/login/', sign_in),

]

urlpatterns = format_suffix_patterns(urlpatterns)
