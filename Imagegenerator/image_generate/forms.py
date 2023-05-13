from django.forms import ModelForm
from django import forms


class LogiChecker(forms.Form):
    userInput  = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': ' Enter your text here'}))
    output = forms.CharField(required=False , widget=forms.Textarea(attrs={'placeholder': ' Output'}))
