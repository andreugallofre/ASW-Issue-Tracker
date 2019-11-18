import textwrap3 as textwrap
import urllib.parse as urlparse
from urllib.parse import parse_qs
from django.contrib import messages
from aswissues import forms
# from flask import Flask, render_template, request
from datetime import date
from .forms import NovaIssueForm, LoginForm, RegisterForm, NovaAttachmentForm, CommentForm
from .models import Issue, User, Comment
from .multiple_form import MultipleFormsView
from .enums import PrioritatSelector

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView




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
        return super(NewIssue, self).form_valid(form)

# DJANGO DETAILED VIEW
#afegir a urls
class DetailedIssue(CreateView, DetailView):
    form_class = CommentForm
    model = Issue
    template_name = 'detailedissue.html'
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # canviar-ho per statuses i no per prioritats!
        context['prioritatSelector'] = PrioritatSelector.__members__
        return context

    def form_valid(self, form):
        form.instance.data_creacio = date.today()
        form.instance.issue = Issue.objects.get(id=1)
        form.instance.owner = User.objects.get(id=1)
        return super(DetailedIssue, self).form_valid(form)
