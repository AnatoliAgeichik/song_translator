from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Singer, Track, User, Translation, Comment
from .utils import LANG_CHOICES


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'spouse_name', 'date_of_birth']


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('name', 'id', 'avatar')


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)


class TrackSerializer(serializers.ModelSerializer):
    singer = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Singer.objects.all()
    )
    original_language = ChoicesField(choices=LANG_CHOICES)

    class Meta:
        model = Track
        fields = ('id', 'track_name', 'text', 'original_language', 'singer', 'file')


class TranslateSerializer(serializers.ModelSerializer):
    language = ChoicesField(choices=LANG_CHOICES)

    class Meta:
        model = Translation
        fields = ('id', 'track_id', 'text', 'language')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'track_id', 'message', 'mark')
