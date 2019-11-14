from django import forms
from django.utils.safestring import mark_safe
from .models import Issue, Attachment

'''
class NovaIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['titol', 'descripcio', 'tipus', 'prioritat']
class NovaAttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['issue','data']
'''

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())



class LoginForm(forms.Form):
    nomUsuari = forms.CharField(label='Usuari', max_length=100)
    clauUsuari = forms.CharField(label='Mot de pas',widget=forms.PasswordInput, max_length=100)


class RegisterForm(forms.Form):
    nomUsuari = forms.CharField(label='Usuari', max_length=100)
    clauUsuari = forms.CharField(label='Mot de pas',widget=forms.PasswordInput, max_length=100)
    emailUsuari = forms.EmailField(label='Correu electrònic', max_length=100)


class NovaIssueForm(forms.Form):
    titol = forms.CharField(label='Usuari', max_length=100)
    descripcio = forms.CharField(max_length=500, widget=forms.TextInput)
    opcionst = (('Bug', 'Bug'),('Millora', 'Millora'),('Tasca', 'Tasca'),('Proposta', 'Proposta'))
    tipus = forms.ChoiceField(choices=opcionst)
    opcionsp = (('Trivial', 'Trivial'),('Menor', 'Menor'),('Major', 'Major'),('Crítica', 'Crítica'),('Bloquejant', 'Bloquejant'))
    prioritat = forms.ChoiceField(choices=opcionsp)

class NovaAttachmentForm(forms.Form):
    data =  forms.FileField()
