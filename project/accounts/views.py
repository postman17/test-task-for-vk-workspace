from django.contrib.auth import get_user_model

from rest_framework import viewsets, mixins

from .serializers import UserSerializer


User = get_user_model()


class UserListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
