from django.contrib.auth import (authenticate, login, get_user_model,logout)
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
import json
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

        if request.is_ajax():
            print(form.errors)
            if not form.errors:
                response_data = {}
                response_data['msg'] = 'Good to go!'
                print(response_data)
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
            if form.errors:
                errors = form.errors.as_json()
                return HttpResponse(errors, status=403, content_type="application/json")

            if user is not None:
                login(request, user)
                return redirect('travel:home')
            else:
                messages.error(request, 'Invalid Credentials')
            return redirect('account:login')
        return render(request, self.template_name, {'form': form})

def register_view(req):
    if req.user.is_authenticated:
        return redirect('travel:home')
    else:
        form = RegisterForm(req.POST or None)
        context = {
            'form': form,
        }
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            newUser = User.objects.create_user(username, email, password)

        if req.is_ajax():
            if not form.errors:
                response_data = {}
                response_data['msg'] = 'Good to go!'
                print(response_data)
                return HttpResponse(json.dumps(response_data),content_type="application/json", status=200)
            if form.errors:
                errors = form.errors.as_json()
                return HttpResponse(errors, status=403, content_type="application/json")
            
        return render(req, "accounts/register.html", context)



def login_view(req):
    if req.user.is_authenticated:
        return redirect('travel:home')
