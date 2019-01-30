from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone
now = timezone.now()


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
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if not location:
            msg = 'Please provide a location'
            self.add_error('location', msg)
        if not description:
            msg = 'No description was provided'
            self.add_error('description', msg)
        if start_date < now:
            msg = 'Start date must be in the future'
            self.add_error('start_date', msg)
        if end_date < now:
            msg = 'End date must be in the future'
            self.add_error('end_date', msg)
        if end_date < start_date:
            msg = 'End date must be after start date'
            self.add_error('end_date', msg)
        return cleaned_data



        """ https://stackoverflow.com/questions/10999021/how-to-convert-gmt-time-to-est-time-using-python """