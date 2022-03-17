from django.db.models import Q

from django_filters import rest_framework as filters

from .models import Article


class ArticleFilterSet(filters.FilterSet):
    tag = filters.CharFilter(field_name='tag__name', lookup_expr='iexact')
    author = filters.CharFilter(method='filter_by_author')

    class Meta:
        model = Article
        fields = ('tag', 'author')

    def filter_by_author(self, queryset, _, value):
        return queryset.filter(Q(author__first_name__iexact=value) | Q(author__last_name__iexact=value))
