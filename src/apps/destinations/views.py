from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core import serializers
from django.shortcuts import HttpResponse, redirect, render

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

import json

from .models import Destination

User = get_user_model()


class HomeView(LoginRequiredMixin,TemplateView):
    redirect_field_name = 'account:home'
    template_name = 'destinations/dashboard.html'

    # form_class = None
    # initial = {'key': 'value'}

    def get_context_data(self, **kwargs):
        obj_list = super(HomeView, self).get_context_data(**kwargs)
        # qs = Destination.objects.all()
        obj_list['user_trips'] =Destination.objects.filter(planner=self.request.user )
        # print(obj_list)
        return obj_list
       
    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST)
        return render(request, self.template_name) #{'form': form})
