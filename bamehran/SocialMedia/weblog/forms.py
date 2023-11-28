from django import forms
from .models import RegisteringModel


class RegisteringForm(forms.ModelForm):
    class Meta:
        model=RegisteringModel
        fields= '__all__'
