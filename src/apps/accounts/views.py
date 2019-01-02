from django.contrib.auth import (authenticate, login, get_user_model,logout)
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm


class LoginFormView(View):
    form_class = LoginForm
    initial = {'key': 'value'}
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('user is ',user)
            if user is not None:
                return redirect('travel:home')
        return render(request, self.template_name, {'form': form})

def register_view(req):
    form = RegisterForm(req.POST or None)
    context = {
        'form': form,
        'content': 'Welcome to the register page!'
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        newUser = User.objects.create_user(username, email, password)
        print(newUser)
    return render(req, "accounts/login.html", context)



def login_view(req):
    if req.user.is_authenticated:
        return redirect('travel:home')

    form = LoginForm(req.POST or None)  # instanciating a form
    context = {
        'form': form,
        'content': 'Welcome to the login page!',
    }
    print("User Logged in", req.user.is_authenticated)
    if form.is_valid():
        # print(form.cleaned_data)
        # using global user object
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(req, username=username,
                            password=password)  # extracts the user
        if user is not None:
            login(req, user)  # this logs in the user
            # Redirect to a success page.
            context['form'] = LoginForm()  # resets the session
            print("User Logged in", req.user.is_authenticated)
            return redirect('travel:home')
        else:
            # Return an 'invalid login' error message.
            print('Error')
    return render(req, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('travel:home')