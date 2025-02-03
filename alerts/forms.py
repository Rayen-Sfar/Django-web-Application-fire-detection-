from django import forms

class ParcelForm(forms.Form):
    parcel_id = forms.CharField(label='Parcel ID', max_length=100)
