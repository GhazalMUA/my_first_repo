from django import forms
class MenuForm(forms.Form):
    item_name=forms.CharField(max_length=30)
    description=forms.CharField(max_length=200)
    category=forms.CharField(max_length=20)