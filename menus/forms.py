from django import forms

# Create your models here.




class MenuForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    stock = forms.BooleanField(required=False)

   


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=60)
