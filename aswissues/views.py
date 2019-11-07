import textwrap3 as textwrap
import urllib.parse as urlparse
from urllib.parse import parse_qs
# from flask import Flask, render_template, request
import datetime
from .forms import NovaIssueForm, LoginForm, RegisterForm

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader


# Create your views here.
class HomePageView(View):
    with open('homepage.html', 'r') as fitxer:
        data = fitxer.read()

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent(data)
        return HttpResponse(response_text)



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


class Issue(View):
    form_class = NovaIssueForm
    initial = {'key': 'value'}
    template_name = 'name.html'

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
                <h1>''' + form.cleaned_data['titol'] + '''</h1>
                '''+form.cleaned_data['descripcio']+'''
                <p>Tipus:<b> '''+form.cleaned_data['tipus']+'''</b>
                Prioritat: <b>'''+form.cleaned_data['prioritat']+'''</b></p>
                </body>
                </html>
              ''')
            # <process form cleaned data>
            return HttpResponse(response_text)
        else:
            return render(request, self.template_name, {'form': form})
