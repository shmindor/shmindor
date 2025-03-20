# etudiants/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur', 'class': 'input input-bordered w-full'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe', 'class': 'input input-bordered w-full'})
    )




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'email', 'sujet', 'message']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['nom', 'description', 'prix', 'image', 'disponible']

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ['nom', 'description', 'date', 'heure', 'prix']

class TableForm (forms.ModelForm):
    class Meta:
        model = Table
        fields = ['numero', 'capacite', 'image']






 

