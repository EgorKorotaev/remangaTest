from django.db.models import F
from django.shortcuts import render
from rest_framework import viewsets, pagination, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import TitleSerializer, VolumeSerializer, ChapterSerializer, TagSerializer
from .models import Title, Volume, Chapter, Tag


class TitleAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().order_by('id')
    serializer_class = TitleSerializer
    pagination_class = TitleAPIListPagination


class VolumeViewSet(viewsets.ModelViewSet):
    queryset = Volume.objects.all().order_by('id')
    serializer_class = VolumeSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all().order_by('id')
    serializer_class = ChapterSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Chapter.objects.get(id=instance.id).increase_view_counter().save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def like(self, request, *args, **kwargs):
        self.get_object().increase_likes_counter().save()
        return Response(status=status.HTTP_200_OK)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('id')
    serializer_class = TagSerializer
