from django import forms
from django.utils.safestring import mark_safe

class NovaIssueForm(forms.Form):
    titol = forms.CharField(label='Títol', max_length=100)
    #descripcio = forms.CharField(label='Descripció', max_length=1000
    descripcio = forms.CharField(widget=forms.Textarea)
    tria1 = (('Bug', 'bug'),('Millora', 'millora'),('Proposta', 'proposta'),('Tasca', 'tasca'),)
    tipus = forms.ChoiceField(label='Tipus',widget=forms.Select,choices=tria1)
    tria2 = (('Trivial', 'Trivial'),('Menor', 'menor'),('Major', 'major'),('Crítica', 'critica'),('Bloquejant', 'bloquejant'),)
    prioritat = forms.ChoiceField(label='Prioritat',widget=forms.Select,choices=tria2)
