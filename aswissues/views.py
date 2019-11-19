import textwrap3 as textwrap
import urllib.parse as urlparse
from urllib.parse import parse_qs
from django.contrib import messages
from aswissues import forms
# from flask import Flask, render_template, request
from datetime import date
from .forms import NovaIssueForm, LoginForm, RegisterForm, NovaAttachmentForm, CommentForm, EditIssueForm
from .models import Issue, User, Comment, Vote
from .multiple_form import MultipleFormsView
from .enums import PrioritatSelector

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader


from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView




# Create your views here.
class HomePageView(ListView):
    model = Issue
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Test2(CreateView):
    model = User
    template_name = 'name.html'
    fields = ['name', 'email']


class Login(View):
    form_class = LoginForm
    initial = {'key': 'value'}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            response_text = textwrap.dedent('''\
                <html>
                <head>
                <title>Issue Creada</title>
                </head>
                <body bgcolor="#E6E6FA">
                ''' + form.cleaned_data['nomUsuari'] + '''
                '''+form.cleaned_data['clauUsuari']+'''
                </body>
                </html>
              ''')
            return HttpResponse(response_text)
        else:
            return render(request, self.template_name, {'form': form})


class Register(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            response_text = textwrap.dedent('''\
                <html>
                <head>
                <title>Usuari creat</title>
                </head>
                <body bgcolor="#E6E6FA">
                ''' + form.cleaned_data['nomUsuari'] + '''
                '''+form.cleaned_data['clauUsuari']+'''
                '''+form.cleaned_data['emailUsuari']+'''
                </body>
                </html>
              ''')
            return HttpResponse(response_text)
        else:
            return render(request, self.template_name, {'form': form})


class NewIssue(CreateView):
    form_class = NovaIssueForm
    model = Issue
    template_name = 'name.html'
    success_url = ''

    def form_valid(self, form):
        form.instance.data_creacio = date.today()
        form.instance.assignee_id = 1
        form.instance.creator_id = 1
        nissue = form.save()
        return redirect('issueDetall', pk=nissue.pk)

        #return super(NewIssue, self).form_valid(form)
def EditarIssue(request, id):
    form_class = EditIssueForm
    instance = get_object_or_404(Issue, id=id)
    form = form_class(request.POST or None, instance=instance)
    if form.is_valid():
        nissue = form.save()
        return redirect('issueDetall', pk=id)
    return render(request, 'edit.html', {'form': form})

class AttachIssue(CreateView, DetailView):
    form_class = NovaAttachmentForm
    model = Issue
    template_name = 'adjuntaFitxer.html'
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # canviar-ho per statuses i no per prioritats-!
        # getting user id to know which comments are their own and stuff
        uid = 1 #change later for self.request.user...
        user = User.objects.get(id=uid)
        context['current_uid'] = uid

        # checking if the user voted the issue
        url = self.request.path
        urlSplit = url.split("/")

        issueID = urlSplit[len(urlSplit)-2]
        issue = Issue.objects.get(id=issueID)

        v = Vote.objects.all().filter(voter=user, issue = issue)
        context['vote'] = not v.exists()

        # checking if the user is watching the issue
        context['watch'] = True
        context['prioritatSelector'] = PrioritatSelector.__members__
        return context

    def form_valid(self, form):
        form.instance.data_creacio = date.today()
        url = self.request.path
        # set success url according to our current one
        self.success_url = url
        # get issue id to bind it to the comment
        urlSplit = url.split("/")
        issueID = urlSplit[len(urlSplit)-2]
        # issue binding
        form.instance.issue = Issue.objects.get(id=issueID)
        #do better
        form.instance.owner = User.objects.get(id=1)
        nissue = form.save()
        return redirect('issueDetall', pk=issueID)
        #return super().form_valid(form)


# DJANGO DETAILED VIEW
class DetailedIssue(CreateView, DetailView):
    form_class = CommentForm
    model = Issue
    template_name = 'detailedissue.html'
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # canviar-ho per statuses i no per prioritats!
        # getting user id to know which comments are their own and stuff
        uid = 1 #change later for self.request.user...
        user = User.objects.get(id=uid)
        context['current_uid'] = uid

        # checking if the user voted the issue
        url = self.request.path
        urlSplit = url.split("/")

        issueID = urlSplit[len(urlSplit)-2]
        issue = Issue.objects.get(id=issueID)

        v = Vote.objects.all().filter(voter=user, issue = issue)
        context['vote'] = not v.exists()

        # checking if the user is watching the issue
        context['watch'] = True
        context['prioritatSelector'] = PrioritatSelector.__members__
        return context

    def form_valid(self, form):
        form.instance.data_creacio = date.today()
        url = self.request.path
        # set success url according to our current one
        self.success_url = url
        # get issue id to bind it to the comment
        urlSplit = url.split("/")
        issueID = urlSplit[len(urlSplit)-2]
        # issue binding
        form.instance.issue = Issue.objects.get(id=issueID)
        #do better
        form.instance.owner = User.objects.get(id=1)
        return super().form_valid(form)

def issue_vote(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    usr = User.objects.get(id=1)
    Vote.objects.create(voter=usr, issue=issue, type=True)
    url = '/issue/'+str(pk)+'/'
    return redirect(url)

def issue_unvote(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    usr = User.objects.get(id=1)
    v = Vote.objects.all().filter(voter=usr, issue = issue)
    v.delete()
    url = '/issue/'+str(pk)+'/'
    return redirect(url)

def issue_watch(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    usr = User.objects.get(id=1)
    Watch.objects.create(voter=usr, issue=issue, type=True)
    url = '/issue/'+str(pk)+'/'
    return redirect(url)

def issue_unwatch(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    usr = User.objects.get(id=1)
    Watch.objects.create(voter=usr, issue=issue, type=True)
    url = '/issue/'+str(pk)+'/'
    return redirect(url)

def delete_comment(request, id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    url = '/issue/'+str(id)+'/'
    return redirect(url)
