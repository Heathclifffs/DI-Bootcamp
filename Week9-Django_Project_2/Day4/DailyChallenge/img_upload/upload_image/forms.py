from django import forms
from .models import Image
from . import models
#.....................................
class ImageForm(forms.ModelForm):
    class Meta:
        model=models.Image
        fields=['image','caption']