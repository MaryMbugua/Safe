from django import forms
from .models import Userm,Neighborhood,Business


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Userm
        exclude = ['user','neighbourhoood','business']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin','occupants_count']
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neigbourhood']
