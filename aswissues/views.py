import textwrap3 as textwrap
import urllib.parse as urlparse
from urllib.parse import parse_qs
from django.contrib import messages
from aswissues import forms
# from flask import Flask, render_template, request
from datetime import date
from .forms import NovaIssueForm, LoginForm, RegisterForm, NovaAttachmentForm
from .models import Issue, User
from .multiple_form import MultipleFormsView


from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView



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

class MultipleFormsDemoView(MultipleFormsView):
    template_name = 'formularimultiple.html'
    success_url = '/'

    # here we specify all forms that should be displayed
    forms_classes = [
        forms.NovaIssueForm,
        forms.NovaAttachmentForm
    ]

    def get_forms_classes(self):
        # we hide staff_only forms from not-staff users
        # our goal no. 3 about dynamic amount list of forms
        forms_classes = super(MultipleFormsDemoView, self).get_forms_classes()
        return forms_classes

    def form_valid(self, form):
        print("yay it's valid!")
        print(form.cleaned_data['Títol'])
        return super(MultipleFormsDemoView, self).form_valid(form)


'''
class Issue(View):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

            i_form = NovaIssueForm(request.POST)
            i_form_valid = i_form.is_valid()
            a_form = NovaAttachmentForm(request.POST,request.FILES)
            a_form_valid = a_form.is_valid()
            if i_form_valid and a_form_valid:
                print("success")
                # process the data
                i_form.instance.data_creacio = date.today()
                i_form.instance.assignee_id = 1
                i_form.instance.creator_id = 1
                i = i_form.save()
                a_form.instance.issue = i
                a = a_form.save()
                return HttpResponseRedirect('/')
    def get(self, request, *args, **kwargs):
        i_form = NovaIssueForm()
        a_form = NovaAttachmentForm()
        return render(request, 'name.html',
                      {'title': 'Nova issue', 'i_form': i_form,
                       'a_form': a_form})
'''
    #form_classes = {'novaissue': NovaIssueForm,
    #                'adjunt': NovaAttachmentForm}
    #template_name = 'name.html'
    #success_url = '/'
