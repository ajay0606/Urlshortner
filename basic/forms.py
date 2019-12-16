from django import forms
from .models import Url

class Urlform(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['original_url',]