from django import forms
"""
class SignUpMerchantForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    description = forms.CharField(label="Description", required=True, widget=forms.Textarea)
    email = forms.EmailField(label="Email", required=True)
    donation = forms.IntegerField(label="Donation", required=True)
"""

from .models import Merchant

class SignUpMerchantForm(forms.ModelForm):
    class Meta:
        model= Merchant
        fields= ["name", "description", "email", "donation"]
