from django.contrib import admin

from .models import Singer, Track, User, Translation


admin.site.register(Singer)
admin.site.register(Track)
admin.site.register(User)
admin.site.register(Translation)
