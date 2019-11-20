import django_filters
from .models import Issue


class IssueFilter(django_filters.FilterSet):
    class Meta:
        model = Issue
        fields = ['titol', 'data_creacio', 'creator', 'assignee', 'tipus', 'prioritat']