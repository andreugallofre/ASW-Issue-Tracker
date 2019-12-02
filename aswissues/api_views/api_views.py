from ..models import Issue, Comment
from rest_framework import viewsets
from ..api_serializers.serializers import IssueSerializer
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
    def retrieve(self,request,pk=None):
         queryset = Comment.objects.filter(pk=pk)
         if not queryset:
             return Response(status=status.HTTP_400_BAD_REQUEST)
         else:
             serializer = CommentSerializer(queryset)
             return Response(serializer.data,status=status.HTTP_200_OK)