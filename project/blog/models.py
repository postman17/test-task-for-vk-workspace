from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=settings.DEFAULT_CHAR_FIELD_MAX_LENGTH)

    class Meta:
        indexes = (models.Index(fields=('name',)),)


class Article(models.Model):
    title = models.CharField(max_length=settings.DEFAULT_CHAR_FIELD_MAX_LENGTH)
    banner = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    richtext = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
