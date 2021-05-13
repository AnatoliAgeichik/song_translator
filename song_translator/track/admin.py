from django.contrib import admin

from .models import Singer, Track, TranslatorUser, Translation


admin.site.register(Singer)
admin.site.register(Track)
admin.site.register(TranslatorUser)
admin.site.register(Translation)
