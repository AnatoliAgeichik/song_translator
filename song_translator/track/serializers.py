from rest_framework import serializers

from .models import Singer, Track


class SingerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Singer
        fields = ('name',)


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    singer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Track
        fields = ('name', 'text', 'translate_text', 'original_language', 'singer')
