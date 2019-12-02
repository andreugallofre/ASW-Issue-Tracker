from ..models import Issue, Comment
from rest_framework import viewsets
from ..api_serializers.serializers import IssueSerializer, CommentSerializer
from rest_framework.response import Response 

class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows issues to be viewed or edited.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows a single comment to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer