from ..models import Issue, Vote, Watch, Comment
from rest_framework import serializers
from social_django import models as oauth_models


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


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    assignee = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    vote_set = VoteSerializer(read_only=True, many=True)
    watch_set = WatcherSerializer(read_only=True, many=True)

    class Meta:
        model = Issue
        fields = ['titol', 'descripcio', 'data_creacio', 'creator', 'assignee',
                  'tipus', 'prioritat', 'status', 'vote_set', 'watch_set']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'issue', 'adjunt']