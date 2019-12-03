from ..models import Issue, Vote, Watch, Comment, User, Attachment
from rest_framework import serializers
from social_django import models as oauth_models
import datetime


class VoteSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.voter.id

    class Meta:
        model = Vote


class WatcherSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.watcher.id

    class Meta:
        model = Watch

class AttachmentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    #adjunt_url = serializers.SerializerMethodField()

    class Meta:
        model = Attachment
        fields = ['issue', 'data_creacio', 'owner', 'data']

    def get_adjunt_url(self, Attachment):
        request = self.context.get('request')
        adjunt_url = Attachment.data.url
        return request.build_absolute_uri(adjunt_url)


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    assignee = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

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
