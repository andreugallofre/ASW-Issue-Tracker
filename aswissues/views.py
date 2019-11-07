import textwrap3 as textwrap
import urllib.parse as urlparse
from urllib.parse import parse_qs
# from flask import Flask, render_template, request
import datetime
from .forms import NovaIssueForm
from .forms import LoginForm
from .forms import RegisterForm

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader


# Create your views here.
class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
                <title>Issue Tracker</title>
            </head>
            <body bgcolor="#E6E6FA">
                <style>
                h1{
                display: inline-block;
                }
                th {
                    text-align: left;
                }
                .button {
                  background-color: #1E90FF;
                  border: none;
                  color: black;
                  padding: 15px 25px;
                  text-align: center;
                  font-size: 16px;
                  cursor: pointer;
                }
                .button:hover {
                  background-color: blue;
                }
                </style>
                    <h1>Issue Tracker</h1>
                    <div style='float: right;'><a href="login">Iniciar Sessió</a></div>
                <form action="issue">
                    <button class="button">Nova Issue</button>
                </form>

                <b>Issues:</b>
                <table class="table table-striped">
                  <tr>
                    <th>Títol</th>
                    <th>Tipus</th>
                    <th>Prioritat</th>
                  </tr>
                  <tr>
                    <td>Prova1</td>
                    <td>Bug</td>
                    <td>Bloquejant</td>
                  </tr>
                  </tr>
                </table>
            </body>
            </html>
        ''')
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
