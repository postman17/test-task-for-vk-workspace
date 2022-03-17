from rest_framework import serializers

from accounts.serializers import ShortUserSerializer

from .models import Tag, Article


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class CreateUpdateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'banner',
            'created_at',
            'updated_at',
            'richtext',
            'tag',
            'author',
        )


class ArticleSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    author = ShortUserSerializer()

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'banner',
            'created_at',
            'updated_at',
            'richtext',
            'tag',
            'author',
        )
