from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core import serializers
from django.shortcuts import (HttpResponse, redirect, render, get_object_or_404)
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.generic import(TemplateView, ListView, DetailView)
from .forms import TripForm

import json

from .models import Destination

User = get_user_model()


class HomeView(LoginRequiredMixin, TemplateView):
    redirect_field_name = 'account:home'
    template_name = 'destinations/dashboard.html'
    # form_class = None
    # initial = {'key': 'value'}

    def get_context_data(self, **kwargs):
        obj_list = super(HomeView, self).get_context_data(**kwargs)
        qs = Destination.objects.all()
        user_results = qs.filter(users_on_trip=self.request.user)
        # print(user_results)
        others_trips = qs.exclude(users_on_trip=self.request.user)
        # print(others_trips)
        obj_list['user_trips'] = user_results
        obj_list['other_users_trips'] = others_trips
        return obj_list

    # Will implement dynamic modal with ajax later
    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST)
        return render(request, self.template_name)  # {'form': form})


class DestinationDetailSlugView(DetailView):
    # queryset = Product.objects.all()
    template_name = "destinations/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Destination.objects.get(slug=slug)  # handling multiple errors
        except Destination.DoesNotExist:
            raise Http404("Not found..")
        except Destination.MultipleObjectsReturned:
            qs = Destination.objects.filter(slug=slug)
            # print(qs)
            instance = qs.first()
        except:
            raise Http404("Something broke ")
        return instance


class AddDestinationFormView(LoginRequiredMixin, TemplateView):
    redirect_field_name = 'account:home'
    form_class = TripForm
    initial = {'key': 'value'}
    template_name = 'destinations/trip_add.html'


    def post(self, request, *args, **kwargs):
        user_pk = request.user.id
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = Destination.objects.new(form, request.user)
            if instance:
                print(instance)
                return redirect('travel:home')
            else:
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial) # do we even need the self.initial??
        return render(request, self.template_name, {'form': form})


def UpdateDestinationView(request):
    destination_id = request.POST.get('destination_id')
    is_planner = request.POST.get('planner')
    user = request.user
    print(is_planner)
    if is_planner:
        try:
            destination_obj = Destination.objects.get(id=destination_id)
        except Destination.DoesNotExist:
            print("Show message to user, Destination is inactive?.")
            return redirect('travel:home')
        if destination_obj:
            destination_obj.delete()
        return redirect('travel:home')

    if destination_id is not None:
        try:
            destination_obj = Destination.objects.get(id=destination_id)
        except Destination.DoesNotExist:
            print("Show message to user, Destination is inactive?.")
            return redirect('travel:home')
        if destination_obj:
            # print(destination_obj.users_on_trip.filter(id=user.id).exists())
            qs = destination_obj.users_on_trip.filter(id=user.id).exists()
            if qs: #check to see if user is in destination
                destination_obj.users_on_trip.remove(request.user.id)
                added = False
            else:
                destination_obj.users_on_trip.add(request.user.id)
                added = True
    if request.is_ajax():
        json_data = {
            "added": added,
            "remove": not added,  # always opposite so true or false
        }
        return JsonResponse(json_data)
        # return JsonResponse({"message":"Error 400"}, status=400)
    return redirect('travel:home')