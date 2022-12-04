from django import forms
from .models import Gif,Category

class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = ['uploader_name', 'title','URL','category']


class Category(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']