from django import forms
from django.core import validators

class Registration_Form(forms.Form):
    First_name=forms.CharField()
    Last_name=forms.CharField()
    Email_id=forms.EmailField()
    Password=forms.CharField()
    Conform_password=forms.CharField()
    Phone_number=forms.IntegerField()
    Gender = forms.CharField()

    # def clean_Password(self):
    #     p=self.cleaned_data['Password']
    #     if p.isdigit():
    #         raise forms.ValidationError('all are digits')
    #     elif len(p) >10:
    #         raise forms.ValidationError('all are characters')
    #     return p

    # def clean_Conform_password(self):
    #     p = self.cleaned_data.get('Password')
    #     cp = self.cleaned_data.get('Conform_password')
    #     print(p,cp)
    #     if p != cp:
    #         raise forms.ValidationError('password not matched')
    #     return cp
