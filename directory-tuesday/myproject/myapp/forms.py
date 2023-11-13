from django import forms
from .models import Logger
from .models import ghaz
from .models import User
SHIFTS = [
        ('1', 'Morning'),
        ('2', 'Afternoon'),
        ('3', 'Evening'),
    ]

class ghaza(forms.ModelForm):
    class Meta:
        model = ghaz
        fields = '__all__'




class Logform (forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
        
        
class userform (forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'