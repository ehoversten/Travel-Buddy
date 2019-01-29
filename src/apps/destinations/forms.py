from django import forms
from django.contrib.auth import get_user_model

class TripForm(forms.Form):
    location = forms.CharField(label="Destination", widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'form_location', "placeholder": "Where are you traveling to?", }))
    description = forms.CharField(label="Description", widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'form_description', 'rows':'3'}))
    start_date = forms.DateTimeField(label='Start Date', widget=forms.DateInput(
        attrs={'type':'date','class': 'form-control', 'id': 'form_start_date'}))
    end_date = forms.DateTimeField(label="End Date", widget=forms.DateInput(
        attrs={'type':'date',"class": "form-control", 'id': 'form_end_date'}))
    
    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        description = cleaned_data.get('description')
        if not location:
            msg = 'Please provide a location'
            self.add_error('location', msg)
        if not description:
            msg = 'No description was provided'
            self.add_error('description', msg)
        return cleaned_data