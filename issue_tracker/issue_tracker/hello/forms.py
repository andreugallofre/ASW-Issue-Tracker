from django import forms

class NovaIssueForm(forms.Form):
    titol = forms.CharField(label='Títol', max_length=100)
    #descripcio = forms.CharField(label='Descripció', max_length=1000
    descripcio = forms.CharField(label='Descripció', max_length=800)


class MyForm(forms.ModelForm):
    class Meta:
        widgets = {
            'my_field': forms.TextInput(attrs={'size': '20'}),
        }
