from django import forms
from .models import ConnectUs

class ConnectUsForm(forms.ModelForm):
    class Meta:
        model = ConnectUs
        fields = ['name', 'phone', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 916 111 22 33'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше сообщение'}),
        }