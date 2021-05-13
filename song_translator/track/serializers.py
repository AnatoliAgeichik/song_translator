from rest_framework import serializers
from enumchoicefield import ChoiceEnum, EnumChoiceField

from .models import Singer, Track, TranslatorUser, Translate
from .utils import LANG_CHOICES


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslatorUser
        fields = ['id', 'email', 'first_name', 'last_name', 'spouse_name', 'date_of_birth']


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('name', 'id')


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)


class TrackSerializer(serializers.ModelSerializer):
    singer = serializers.StringRelatedField(many=True)
    original_language = ChoicesField(choices=LANG_CHOICES)

    class Meta:
        model = Track
        fields = ('id', 'name', 'text', 'original_language', 'singer')


class TranslateSerializer(serializers.ModelSerializer):
    language = ChoicesField(choices=LANG_CHOICES)

    class Meta:
        model = Translate
        fields = ('id', 'track_id', 'text', 'language')
