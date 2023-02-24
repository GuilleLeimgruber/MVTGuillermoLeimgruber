from django import forms

# Create your models here.




class ProviderForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=300)
    phone = forms.CharField(max_length=20)
    tax_category = forms.CharField(max_length=50)