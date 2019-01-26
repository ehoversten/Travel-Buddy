from django import forms

class TripForm(forms.Form):
    location = forms.CharField(label="Destination", widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'form_location', "placeholder": "Where are you traveling to?", }))
    description = forms.CharField(label="Description", widget=forms.Textarea(
        attrs={"class": "form-control", 'id': 'form_description', 'rows':'3'}))
    start_date = forms.DateTimeField(label="Start Date", widget=forms.DateInput(
        attrs={"class": "form-control", 'id': 'form_start_date'}))
    end_date = forms.DateTimeField(label="End Date", widget=forms.DateInput(
        attrs={"class": "form-control", 'id': 'form_end_date'}))
    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #     try:
    #         user = User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         user = None
    #     # print(user)
    #     if user is None:
    #             msg = 'Please register first'
    #             self.add_error('username', msg)
    #     else:
    #         # print(not user.check_password(password))
    #         if not user.check_password(password):
    #             userError = 'Invalid Credentials'
    #             self.add_error('password', userError)
    #     return cleaned_data