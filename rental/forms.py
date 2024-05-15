
from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['drone', 'user', 'rental_date', 'return_date', 'is_deleted']
        widgets = {
            'rental_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'return_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }