from django.contrib.auth import (authenticate, login, get_user_model,logout)
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm

User = get_user_model()

class LoginFormView(View):
    form_class = LoginForm
    initial = {'key': 'value'}
    template_name = 'accounts/login.html'
    def get(self, request, *args, **kwargs):
        if request.user is not None:
            if request.user.is_authenticated:
                return redirect('travel:home')
        else:
            return redirect('account:login')
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('travel:home')
        return render(request, self.template_name, {'form': form})

def register_view(req):
    form = RegisterForm(req.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        newUser = User.objects.create_user(username, email, password)
    return render(req, "accounts/login.html", context)



def login_view(req):
    if req.user.is_authenticated:
        return redirect('travel:home')
