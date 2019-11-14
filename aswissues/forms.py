from django import forms
from django.utils.safestring import mark_safe
from .models import Issue, Comment


class NovaIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['titol', 'descripcio', 'tipus', 'prioritat']


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