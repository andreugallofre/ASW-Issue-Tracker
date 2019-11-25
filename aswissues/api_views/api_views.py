from ..models import Issue
from rest_framework import viewsets
from ..api_serializers.serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows issues to be viewed or edited.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
