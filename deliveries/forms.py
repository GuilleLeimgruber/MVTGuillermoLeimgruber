from django import forms








class DeliveryForm(forms.Form):
    

    client = forms.CharField(max_length=100)
    menu = forms.CharField(max_length=100)
   # create_time = forms.DateTimeField()
    payment_method = forms.CharField(max_length=13)
