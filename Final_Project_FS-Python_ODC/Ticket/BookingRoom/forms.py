from django.forms import ModelForm
from .models import *


class RoomForm(ModelForm):
    class Meta:
        model= Room
        fields= '__all__'

class MovieForm(ModelForm):
    class Meta:
        model= Movie
        fields= '__all__'

class PlateForm(ModelForm):
    class Meta:
        model= Plate
        fields= '__all__'        

class ChamberForm(ModelForm):
    class Meta:
        model= Chamber
        fields= '__all__'

class RestauForm(ModelForm):
    class Meta:
        model= Restauplace
        fields= '__all__'        