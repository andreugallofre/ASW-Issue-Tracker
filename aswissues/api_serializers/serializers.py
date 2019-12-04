from ..models import Issue, Vote, Watch, Comment, User, Attachment
from rest_framework import serializers
# from django.db import User as test
from django.contrib.auth.models import User as social_users
import datetime


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    voter = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    issue = serializers.PrimaryKeyRelatedField(many=False, queryset=Issue.objects.all())
    type = serializers.BooleanField(read_only= True)

    class Meta:
        model = Vote
        fields = ['issue', 'voter', 'type']

class WatcherSerializer(serializers.RelatedField):
    watcher = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    issue = serializers.PrimaryKeyRelatedField(many=False, queryset=Issue.objects.all())
    type = serializers.BooleanField(read_only= True)

    class Meta:
        model = Watch
        fields = ['issue', 'watcher', 'type']

class AttachmentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # adjunt_url = serializers.SerializerMethodField()

    class Meta:
        model = Attachment
        fields = ['issue', 'data_creacio', 'owner', 'data']

    def get_adjunt_url(self, Attachment):
        request = self.context.get('request')
        adjunt_url = Attachment.data.url
        return request.build_absolute_uri(adjunt_url)


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    assignee = serializers.PrimaryKeyRelatedField(many=False, queryset=social_users.objects.all())

    vote_set = VoteSerializer(read_only=True, many=True)
    watch_set = WatcherSerializer(read_only=True, many=True)

    class Meta:
        model = Issue
        fields = ['titol', 'descripcio', 'data_creacio', 'creator', 'assignee',
                  'tipus', 'prioritat', 'status', 'vote_set', 'watch_set']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = ['content', 'issue', 'adjunt', 'data_creacio', 'owner']


class UserSerializer(serializers.RelatedField):
    class Meta:
        model = User
        fields = ['name, email']
