from django import forms
from .emailTypes import approvedEmails
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'form_username', "placeholder": "Your Username", }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "form-control", 'id': 'form_password', "placeholder": "Your Password", }))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user is None:
            msg = 'Please register first'
            self.add_error('username', msg)
        else:
            if not user.check_password(password):
                userError = 'Invalid Credentials'
                self.add_error('password', userError)
        return cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'form_username', "placeholder": "Your Username", }))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control", 'id': 'form_email', "placeholder": "Your email", }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'id': 'form_password'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(
        attrs={"class": "form-control", 'id': 'form_password2'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password2 = cleaned_data.get('password2')
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')

        if password and password2:
            if password2 != password:
                msg = 'Passwords must match'
                self.add_error('password', msg)
        if User.objects.filter(email=email).exists():
            userError = 'Email Already Taken'
            self.add_error('password', userError)

        return cleaned_data
