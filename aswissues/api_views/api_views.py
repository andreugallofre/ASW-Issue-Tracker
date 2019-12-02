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
    serializer_class = CommentSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Comment.objects.all()
        nissue = self.request.query_params.get('issue', None)
        if nissue is not None:
            queryset = queryset.filter(issue__id=nissue)
        return queryset
