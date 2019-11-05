import textwrap
import urllib.parse as urlparse
from urllib.parse import parse_qs
#from flask import Flask, render_template, request
import datetime
from .forms import NovaIssueForm
#from flask import request

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader


class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Issue Tracker</title>
            </head>
            <body bgcolor="#E6E6FA">
                <style>
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
                <form action="issue">
                 <button class="button">Nova Issue</button>
                </form>
                <b>Issues:</b>

            </body>
            </html>
        ''')
        return HttpResponse(response_text)


class NovaIssue(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
                  <head>
                      <title>Nova Issue</title>
                  </head>
                  <body>
                    <h1>Nova Issue</h1>

                     <form action="issue" method="post">
                      <style>
                      label {
                        display: inline-block;
                        width: 140px;
                        text-align: left;
                      }​
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
                      <label>Títol</label>
                      <input name= "text" type="text"><br>
                      <label>Descripció</label>
                      <textarea name="comment" rows="10" cols="50">Expliqueu l'issue...</textarea><br>
                      <label>Tipus</label>
                        <select name="tipus">
                          <option value="bug">Bug</option>
                          <option value="millora">Millora</option>
                          <option value="proposta">Proposta</option>
                          <option value="tasca">Tasca</option>
                        </select><br>
                      <label>Prioritat</label>
                      <select name="prioritat">
                        <option value="trivial">Trivial</option>
                        <option value="menor">Menor</option>
                        <option value="major">Major</option>
                        <option value="critica">Crítica</option>
                        <option value="bloquejant">Bloquejant</option>
                      </select><br>
                    <button class="button">Crear issue</button>
                    </form>

                  </body>
            </html>
        ''')
        return HttpResponse(response_text)


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
