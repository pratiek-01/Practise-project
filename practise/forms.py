from django import forms

class userForm(forms.Form):
    Name=forms.CharField()
    Contact=forms.CharField()
    Email=forms.EmailField()
    Address=forms.CharField()