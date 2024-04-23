from django import forms
from .models import Category

class JobSearchForm(forms.Form):
    keywords = forms.CharField(
        max_length=100, 
        required=False, 
        label='Keywords',
        widget=forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Keywords'})
    )
    location = forms.CharField(
        max_length=100, 
        required=False, 
        label='Location',
        widget=forms.TextInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'Location'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        required=False, 
        label='Category',
        widget=forms.Select(attrs={'class': 'form-control shadow-none'})
    )
