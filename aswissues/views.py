import textwrap3 as textwrap
import urllib.parse as urlparse
import os
from urllib.parse import parse_qs
# from flask import Flask, render_template, request
from datetime import date
from .forms import NovaIssueForm, LoginForm, RegisterForm
from .models import Issue

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from django.views.generic.base import View
from django.views.generic.edit import CreateView

# Create your views here.
class HomePageView(View):
    def dispatch(self, request, *args, **kwargs):
        template = loader.get_template("homepage.html")
        return HttpResponse(template.render())



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


class Issue(CreateView):
    form_class = NovaIssueForm
    model = Issue
    template_name = 'name.html'

    def form_valid(self, form):
        form.instance.data_creacio = date.today()
        form.instance.assignee_id = 1
        form.instance.creator_id = 1
        return super(Issue, self).form_valid(form)
