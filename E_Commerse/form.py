from django import forms
from .models import *

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','rating','comment']
        
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['First_Name','Last_Name','Gender','Email','Phone_Number']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)  # Field for the username
    password = forms.CharField(widget=forms.PasswordInput)
    
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']  # Collecting username and email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("The passwords do not match.")
        return cleaned_data

class addressform(forms.ModelForm):
        class Meta:
            model = Address
            fields = ['Name', 'contact_no', 'Address_Line1', 'Address_Line2', 'City', 'State', 'Zip_Code', 'Pin_Code']
            widgets = {
                'Name': forms.TextInput(attrs={'class': 'form-control'}),
                'contact_no': forms.NumberInput(attrs={'class': 'form-control'}),
                'Address_Line1': forms.TextInput(attrs={'class': 'form-control'}),
                'Address_Line2': forms.TextInput(attrs={'class': 'form-control'}),
                'City': forms.TextInput(attrs={'class': 'form-control'}),
                'State': forms.Select(attrs={'class': 'form-control'}),
                'Zip_Code': forms.TextInput(attrs={'class': 'form-control'}),
                'Pin_Code': forms.TextInput(attrs={'class': 'form-control'}),
            }

class ProductSearch(forms.Form):
    query = forms.CharField(max_length=100,required=False,label='Search Products...')
