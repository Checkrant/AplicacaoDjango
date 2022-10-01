from django import forms
from django.forms import fields, models
from .models import User, UserRant

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'email', 'password']
        
class rantForm(forms.ModelForm):
    class Meta:
        model = UserRant
        fields = ['nomeRant', 'endereco', 'horarioInicio', 'horarioFinal', 'tipo']



