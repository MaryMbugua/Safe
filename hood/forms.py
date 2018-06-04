from django import forms
from .models import Userm,Neighborhood,Business,Post


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Userm
        exclude = ['user']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author','post_date']
