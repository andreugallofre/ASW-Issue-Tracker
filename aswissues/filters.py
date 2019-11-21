import django_filters
from .models import Issue, Watch

class IssueFilter(django_filters.FilterSet):
    class Meta:
        model = Issue
        fields = ['titol', 'data_creacio', 'creator', 'assignee', 'status', 'creator', 'tipus', 'watch__watcher', 'prioritat']