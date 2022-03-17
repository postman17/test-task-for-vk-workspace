from django.urls import include, path

from rest_framework.routers import DefaultRouter

from accounts.views import UserListView
from blog.views import TagViewSet, ArticleViewSet


router = DefaultRouter()
router.register(r'users', UserListView, basename='user')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'articles', ArticleViewSet, basename='article')


urlpatterns = [
    path("", include((router.urls, None)), name="routers"),
]
