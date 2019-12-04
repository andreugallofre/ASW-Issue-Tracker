from ..models import Issue, Comment, Attachment, Vote, Watch
from rest_framework import viewsets
from ..api_serializers.serializers import IssueSerializer, CommentSerializer, AttachmentSerializer, VoteSerializer, WatcherSerializer
from rest_framework.response import Response
from rest_framework import filters


class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows issues to be viewed or edited.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titol', 'descripcio', 'data_creacio',
                     'tipus', 'prioritat', 'status']
    ordering_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttachmentViewSet(viewsets.ModelViewSet):
    # queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        # serializer_class = AttachmentSerializer(Attachment, context={"request":self.request})
        queryset = Attachment.objects.all()
        nissue = self.request.query_params.get('issue', None)
        if nissue is not None:
            queryset = queryset.filter(issue__id=nissue)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VotesViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(voter=self.request.user)
        serializer.save(type=True)

class WatchersViewSet(viewsets.ModelViewSet):
    serializer_class = WatcherSerializer
    queryset = Watch.objects.all()

    def perform_create(self, serializer):
        serializer.save(watcher=self.request.user)
        serializer.save(type=True)
