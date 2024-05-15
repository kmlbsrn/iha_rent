# forms.py

from django import forms
from .models import Drone

class ProductForm(forms.ModelForm):
    class Meta:
        model = Drone
        fields = ['brand', 'model', 'weight', 'category']

