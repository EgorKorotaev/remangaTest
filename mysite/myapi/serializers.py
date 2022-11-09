# serializers.py
from rest_framework import serializers

from .models import Title, Volume, Chapter, Tag


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    volume = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'ru_name', 'en_name', 'alt_name', 'description', 'tags', 'volume')

    def get_volume(self, obj):
        return VolumeSerializer(obj.title_volume, context=self.context, many=True).data


class VolumeSerializer(serializers.HyperlinkedModelSerializer):
    chapter = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Volume
        fields = ['id', 'title', 'name', 'cost', 'number', 'chapter']

    def get_chapter(self, obj):
        return ChapterSerializer(obj.volume_chapter, context=self.context, many=True).data


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'volume', 'number', 'content', 'view_counter', 'likes_counter')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
