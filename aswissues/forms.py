from django import forms
from django.utils.safestring import mark_safe


class NovaIssueForm(forms.Form):
    titol = forms.CharField(label='Títol', max_length=100)
    # descripcio = forms.CharField(label='Descripció', max_length=1000
    descripcio = forms.CharField(label='Descripció',widget=forms.Textarea)
    tria1 = (('Bug', 'bug'),('Millora', 'millora'),('Proposta', 'proposta'),('Tasca', 'tasca'),)
    tipus = forms.ChoiceField(label='Tipus', widget=forms.Select, choices=tria1)
    tria2 = (('Trivial', 'Trivial'),('Menor', 'menor'), ('Major', 'major'), ('Crítica', 'critica'), ('Bloquejant', 'bloquejant'),)
    prioritat = forms.ChoiceField(label='Prioritat', widget=forms.Select, choices=tria2)


class LoginForm(forms.Form):
    nomUsuari = forms.CharField(label='Usuari', max_length=100)
    clauUsuari = forms.CharField(label='Mot de pas',widget=forms.PasswordInput, max_length=100)

class RegisterForm(forms.Form):
    nomUsuari = forms.CharField(label='Usuari', max_length=100)
    clauUsuari = forms.CharField(label='Mot de pas',widget=forms.PasswordInput, max_length=100)
    emailUsuari = forms.EmailField(label='Correu electrònic', max_length=100)
