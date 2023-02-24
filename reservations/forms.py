from django import forms






class ReservationsForm(forms.Form):
    name = forms.CharField(max_length=100)
    dinner = forms.IntegerField()
    reservation_date = forms.DateField()