from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Tag, Article
from .serializers import TagSerializer, ArticleSerializer, CreateUpdateArticleSerializer
from .filters import ArticleFilterSet


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.order_by('id')
    serializer_class = ArticleSerializer
    search_fields = ('title', 'tag__name', 'author__first_name', 'author__last_name')
    filterset_class = ArticleFilterSet

    def create(self, request, *args, **kwargs):
        serializer = CreateUpdateArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        response_serializer = self.get_serializer(instance=instance)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = CreateUpdateArticleSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
