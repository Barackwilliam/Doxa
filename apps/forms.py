from django import forms
from .models import CustomerMessage

class MyMessage(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = ['full_name', 'email', 'subject', 'message']
