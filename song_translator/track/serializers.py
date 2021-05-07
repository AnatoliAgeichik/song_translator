from rest_framework import serializers

from .models import Singer, Track, TranslatorUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslatorUser
        fields = ['id', 'email', 'first_name', 'last_name', 'spouse_name', 'date_of_birth']


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('name', 'id')


class TrackSerializer(serializers.ModelSerializer):
    singer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Track
        fields = ('id', 'name', 'text', 'translate_text', 'original_language', 'singer')
