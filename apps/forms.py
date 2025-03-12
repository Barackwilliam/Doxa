from django import forms
from .models import Message

class MyMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['full_name','email','phone_number','subject','message']

