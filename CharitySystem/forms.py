from django import forms
from .models import Donation, FundRequest, NGO  # Make sure to import NGO model


# DonationForm for donors to make donations
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor_name', 'email', 'amount', 'payment_method', 'message']
        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }


# FundRequestForm for NGOs to request funds
class FundRequestForm(forms.ModelForm):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, required=True)

    class Meta:
        model = FundRequest
        fields = ['ngo', 'title', 'description', 'amount_needed', 'payment_method']
        widgets = {
            'ngo': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'amount_needed': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }


# NGOForm for NGOs to register and get verified
class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['name', 'email', 'verification_docs']  # Adjust the fields as per the NGO model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'verification_docs': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
