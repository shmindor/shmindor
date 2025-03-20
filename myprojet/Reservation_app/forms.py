from django import forms
from myapp.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'heure', 'menu']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-2 border rounded-lg'}),
            'heure': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-3 py-2 border rounded-lg'}),
            'menu': forms.SelectMultiple(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        }
