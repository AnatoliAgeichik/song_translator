from django.contrib import admin

from .models import Singer, Track, User, Translation, Comment


admin.site.register(Singer)
admin.site.register(Track)
admin.site.register(User)
admin.site.register(Translation)
admin.site.register(Comment)