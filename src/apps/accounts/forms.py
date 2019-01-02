from django import forms
from .emailTypes import approvedEmails
from django.contrib.auth import get_user_model
User = get_user_model()

class ContactForm(forms.Form):
    full_name = forms.CharField(label="Full Name", widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'form_full_name', "placeholder": "Your full name", }))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control", 'id': 'form_email', "placeholder": "Your email", }))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", 'id': 'form_contact_message', "placeholder": "Your message", }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        temp_email = email.split('@')[1]

        if temp_email not in approvedEmails:
            raise forms.ValidationError("Email has to be valid..see list.")

        return email

    # def clean_content(self):
    #     raise forms.ValidationError("Content is wrong.")


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={"class": "form-control", 'id': 'form_username', "placeholder": "Your Username", }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "form-control", 'id': 'form_password'}))


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
        # Queryset
        if User.objects.filter(username=username).exists(): 
            raise forms.ValidationError("Username is taken")
        return username

    def clean(self):
        print(self)
        cleaned_data = super().clean()
        password2 = cleaned_data.get('password2')
        password = cleaned_data.get('password')
        username = cleaned_data.get('username')
        print(password, password2)
        if password and password2:
            if password2 != password:
                msg = 'Passwords must match'
                self.add_error('password', msg)

        return cleaned_data
