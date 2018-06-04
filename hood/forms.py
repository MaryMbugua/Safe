from django import forms
from .models import Userm,Neighborhood,Business


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Userm
        exclude = ['user']

