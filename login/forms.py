from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your full name"}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your phone number"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your home address"}))
    class Meta:
        model = UserProfile
        fields = ('full_name', 'phone_no', 'address')