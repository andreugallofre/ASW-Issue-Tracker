from django.db import models
from social_django import models as oauth_models
from .enums import TipusSelector, PrioritatSelector, StatusSelector
from datetime import date

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Issue(models.Model):
    titol = models.CharField(max_length=200)
    descripcio = models.TextField()
    data_creacio = models.DateField()
    creator = models.ForeignKey(oauth_models.USER_MODEL, related_name='Creator', on_delete=models.CASCADE)
    assignee = models.ForeignKey(oauth_models.USER_MODEL, related_name='Assignee', on_delete=models.CASCADE, null=True, blank=True)
    tipus = models.CharField(
      max_length=20,
      choices=[(tag.name, tag.value) for tag in TipusSelector],
      default=TipusSelector.Millora
    )
    prioritat = models.CharField(
      max_length=20,
      choices=[(tag.name, tag.value) for tag in PrioritatSelector],
      default=PrioritatSelector.Trivial
    )
    adjunt = models.FileField(blank=True)

    status = models.CharField(
      max_length=20,
      choices=[(tag.name, tag.value) for tag in StatusSelector],
      default=StatusSelector.Obert
    )


class Attachment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    data_creacio = models.DateField()
    owner = models.ForeignKey(oauth_models.USER_MODEL, on_delete=models.CASCADE)
    data = models.FileField()


class Comment(models.Model):
    content = models.TextField()
    data_creacio = models.DateField(auto_now=True, null=False, blank=False)
    owner = models.ForeignKey(oauth_models.USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    adjunt = models.ForeignKey(Attachment,on_delete=models.CASCADE,null=True)
    @classmethod
    def create(cls, owner,issue,data,adjunt):
        comment = cls(owner=owner,issue=issue,data_creacio=data,adjunt=adjunt)
        return comment


class Vote(models.Model):
    voter = models.ForeignKey(oauth_models.USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    type = models.BooleanField()


class Watch(models.Model):
    watcher = models.ForeignKey(oauth_models.USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    type = models.BooleanField()
