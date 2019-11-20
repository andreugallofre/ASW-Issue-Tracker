from django import forms
from django.utils.safestring import mark_safe
from .models import Issue, Attachment, Comment
from crispy_forms.helper import FormHelper


class NovaAttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['issue','data']



class NovaIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['titol', 'descripcio', 'tipus', 'prioritat','adjunt']

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class LoginForm(forms.Form):
    nomUsuari = forms.CharField(label='Usuari', max_length=100)
    clauUsuari = forms.CharField(label='Mot de pas',widget=forms.PasswordInput, max_length=100)


class RegisterForm(forms.Form):
    nomUsuari = forms.CharField(label='Usuari', max_length=100)
    clauUsuari = forms.CharField(label='Mot de pas',widget=forms.PasswordInput, max_length=100)
    emailUsuari = forms.EmailField(label='Correu electrònic', max_length=100)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class NewIssueForm(forms.Form):
    titol = forms.CharField(label='Títol', max_length=100)
    descripcio = forms.CharField(max_length=500, widget=forms.TextInput)
    opcionst = (('Bug', 'Bug'),('Millora', 'Millora'),('Tasca', 'Tasca'),('Proposta', 'Proposta'))
    tipus = forms.ChoiceField(choices=opcionst)
    opcionsp = (('Trivial', 'Trivial'),('Menor', 'Menor'),('Major', 'Major'),('Crítica', 'Crítica'),('Bloquejant', 'Bloquejant'))
    prioritat = forms.ChoiceField(choices=opcionsp)

class NovaAttachmentForm(forms.Form):
    Fitxer =  forms.FileField()

class IssueListFormHelper(FormHelper):
    model = Issue
    form_tag = False


