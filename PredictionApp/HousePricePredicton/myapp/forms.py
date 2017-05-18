from django import forms


class UserForm(forms.Form):
    bedrooms = forms.CharField(required=True)
    bathrooms = forms.CharField(required=True)
    sqft_living= forms.CharField(required=True)
    sqft_lot = forms.CharField(required=True)
    floors = forms.CharField(required=True)
    yr_built = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)