from . import models
from django import forms
from django.contrib.auth import get_user_model
from .models import Avis,Chambre,Reservation,Message
# from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin
#........................................
class AvisForm(forms.ModelForm):
    class Meta:
        model=models.Avis
        fields=['content']
        # long_text = forms.Textarea(widget=EmojiPickerTextareaAdmin)
class DeleteAvisForm(forms.Form):
    delete_avis= forms.BooleanField(widget=forms.HiddenInput, initial=True)
#...................................
class ReservationForm(forms.ModelForm):
    edit_reservation = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model=models.Reservation
        fields=['date_reservation','dure_sejour','reservation']
        
class DeleteReservationForm(forms.Form):
    delete_reservation= forms.BooleanField(widget=forms.HiddenInput, initial=True)         
#....................................................
class MessageForm(forms.ModelForm):
    edit_message = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model=models.Message
        fields=['nom','email','content']
        
class DeleteMessageForm(forms.Form):
    delete_message= forms.BooleanField(widget=forms.HiddenInput, initial=True) 