from django import forms
from .models import Contact





class ReviewForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['reviews']
