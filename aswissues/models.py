from django.db import models
from .enums import TipusSelector, PrioritatSelector




class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Issue(models.Model):
    titol = models.CharField(max_length=200)
    descripcio = models.TextField()
    data_creacio = models.DateField()
    creator = models.ForeignKey(User, related_name='Creator',  on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name='Assignee', on_delete=models.CASCADE)
    watchers = models.ManyToManyField(User)
    tipus = models.CharField(
      max_length=20,
      choices=[(tag.name, tag.value) for tag in TipusSelector],  # Choices is a list of Tuple
      default=TipusSelector.Millora
    )
    prioritat = models.CharField(
      max_length=20,
      choices=[(tag.name, tag.value) for tag in PrioritatSelector],  # Choices is a list of Tuple
      default=PrioritatSelector.Trivial
    )
    adjunt = models.FileField(upload_to="media",blank=True)



class Comment(models.Model):
    content = models.TextField()
    data_creacio = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)


class Attachment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    data = models.FileField()


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    type = models.BooleanField()
