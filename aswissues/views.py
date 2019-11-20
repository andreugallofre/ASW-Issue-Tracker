import textwrap3 as textwrap
import urllib.parse as urlparse
from urllib.parse import parse_qs
from django.contrib import messages
from aswissues import forms
# from flask import Flask, render_template, request
from datetime import date
from .forms import NovaIssueForm, LoginForm, RegisterForm, NovaAttachmentForm, CommentForm, EditIssueForm
from .models import Issue, Comment, Vote, Watch
from social_django import models as oauth_models
from .multiple_form import MultipleFormsView
from .enums import PrioritatSelector, StatusSelector

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib import auth

from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django_tables2 import SingleTableView
from .tables import IssueTable
from .forms import IssueListFormHelper
from .filters import IssueFilter
from .utils import PagedFilteredTableView


class HomePageView(PagedFilteredTableView):
    model = Issue
    table_class = IssueTable
    template_name = 'homepage.html'
    filter_class = IssueFilter
    formhelper_class = IssueListFormHelper

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        qs = super(HomePageView, self).get_queryset()
        return list(qs)

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
        form.instance.creator_id = self.request.user.id
        form.instance.status = StatusSelector.Nou.value
        nissue = form.save()
        return redirect('issueDetall', pk=nissue.pk)


def EditarIssue(request, id):
    form_class = EditIssueForm
    instance = get_object_or_404(Issue, id=id)
    form = form_class(request.POST or None, instance=instance)
    if form.is_valid():
        issue = get_object_or_404(Issue, pk=id)

        if issue.prioritat != form.instance.prioritat:
            change_priority_comment(request.user, issue, form.instance.prioritat)

        if issue.tipus != form.instance.tipus:
            change_tipus_comment(request.user, issue, form.instance.tipus)

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

        user = self.request.user.id
        context['current_uid'] = user

        # checking if the user voted the issue
        url = self.request.path
        urlSplit = url.split("/")

        issueID = urlSplit[len(urlSplit)-2]
        issue = Issue.objects.get(id=issueID)

        v = Vote.objects.all().filter(voter=user, issue=issue)
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
        # do better
        form.instance.owner = self.request.user
        nissue = form.save()
        comment = Comment.create(nissue.owner, nissue.issue, nissue.data_creacio, nissue)
        comment.content = "S'ha adjuntat un nou fitxer:"
        comment.save()
        return redirect('issueDetall', pk=issueID)


class ChangeState(CreateView, DetailView):
    print("holita")
    form_class = CommentForm
    model = Issue
    template_name = 'canviaEstat.html'
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # canviar-ho per statuses i no per prioritats-!
        # getting user id to know which comments are their own and stuff

        user = self.request.user.id
        context['current_uid'] = user

        # checking if the user voted the issue
        url = self.request.path
        urlSplit = url.split("/")

        issueID = urlSplit[len(urlSplit)-2]
        issue = Issue.objects.get(id=issueID)

        v = Vote.objects.all().filter(voter=user, issue=issue)
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
        status = urlSplit[len(urlSplit)-1]
        issueID = urlSplit[len(urlSplit)-2]
        # issue binding
        issue_to_bind = Issue.objects.get(id=issueID)

        if issue_to_bind.status != status:
            form.instance.issue = issue_to_bind
            # do better
            form.instance.owner = self.request.user
            form.instance.content = "Estat canviat: <a href='/?status=" + status + "'>" + status + "</a><br>" + form.instance.content
            issue_to_bind.status = status
            issue_to_bind.save()
            nissue = form.save()
            return redirect('issueDetall', pk=issueID)

        return redirect('issueDetall', pk=issueID)

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
        user = self.request.user.id
        context['current_uid'] = user

        # checking if the user voted the issue
        url = self.request.path
        urlSplit = url.split("/")

        issueID = urlSplit[len(urlSplit)-2]
        issue = Issue.objects.get(id=issueID)

        v = Vote.objects.all().filter(voter=user, issue = issue)
        context['vote'] = not v.exists()
        nv = Vote.objects.filter(issue=issue)
        if nv is None:
            nv = 0
        else:
            nv = len(nv)
        context['nvotes'] = nv

        # checking if the user is watching the issue
        w = Watch.objects.all().filter(watcher=user, issue = issue)
        context['watch'] = not w.exists()
        nw = Watch.objects.filter(issue=issue)
        if nw is None:
            nw = 0
        else:
            nw = len(nw)
        context['nwatch'] = nw
        context['prioritatSelector'] = PrioritatSelector.__members__
        context['statusSelector'] = StatusSelector.__members__

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
        form.instance.owner = self.request.user
        return super().form_valid(form)


def issue_vote(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    usr = request.user
    Vote.objects.create(voter=usr, issue=issue, type=True)
    url = '/issue/'+str(pk)+'/'
    return redirect(url)


def issue_unvote(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    usr = request.user
    v = Vote.objects.all().filter(voter=usr, issue = issue)
    v.delete()
    url = '/issue/'+str(pk)+'/'
    return redirect(url)


def issue_unwatch(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    usr = request.user
    w = Watch.objects.all().filter(watcher=usr, issue = issue)
    w.delete()
    url = '/issue/'+str(pk)+'/'
    return redirect(url)


def issue_watch(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    usr = request.user
    Watch.objects.create(watcher=usr, issue=issue, type=True)
    url = '/issue/'+str(pk)+'/'
    return redirect(url)


def issue_delete(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    issue.delete()
    url = '/'
    return redirect(url)


def delete_comment(request, id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    url = '/issue/'+str(id)+'/'
    return redirect(url)


def update_comment(request, id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    c = request.POST['formContent']
    if c is not None:
        comment.content = c
        comment.save(update_fields=["content"])
    url = '/issue/'+str(id)+'/'
    return redirect(url)


def change_state(request, id, status):
    issue = get_object_or_404(Issue, pk=id)
    print(request.user)
    comment = Comment.create(request.user, issue, date.today(), None)
    comment.content = "Estat canviat: <a href='/?status=" + status + "'>" + status
    comment.save()

    issue.status = StatusSelector[status].value
    issue.save()
    url = '/issue/' + str(id) + '/'
    return redirect(url)


def change_priority_comment(user, issue, prioritat):
    comment = Comment.create(user, issue, date.today(), None)
    comment.content = "Marcat com: <a href='/?prioritat=" + prioritat + "'>" + prioritat + "</a>"
    comment.save()
    return None


def change_tipus_comment(user, issue, tipus):
    comment = Comment.create(user, issue, date.today(), None)
    comment.content = "Marcat com: <a href='/?tipus=" + tipus + "'>" + tipus + "</a>"
    comment.save()
    return None
