from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Singer, Track, User, Translation, Comment
from .utils import LANG_CHOICES


def get_user_from_request(requests):
    user = None
    if requests and hasattr(requests, "user"):
        user = requests.user
    return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'spouse_name', 'date_of_birth']


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('name', 'id', "owner", "avatar")

    def create(self, validated_data):
        user = get_user_from_request(self.context.get("request"))
        validated_data['owner'] = user
        return super().create(validated_data)


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
        fields = ('id', 'track_name', 'text', 'original_language', 'singer', 'owner', 'file')

    def create(self, validated_data):
        user = get_user_from_request(self.context.get("request"))
        validated_data['owner'] = user
        return super().create(validated_data)


class TranslateSerializer(serializers.ModelSerializer):
    language = ChoicesField(choices=LANG_CHOICES)

    class Meta:
        model = Translation
        fields = ('id', 'track_id', 'text', 'language', 'owner')

    def create(self, validated_data):
        user = get_user_from_request(self.context.get("request"))
        validated_data['owner'] = user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'track_id', 'message', 'mark', 'owner')

    def create(self, validated_data):
        user = get_user_from_request(self.context.get("request"))
        validated_data['owner'] = user
        return super().create(validated_data)
