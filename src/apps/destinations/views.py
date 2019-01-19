from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render
from django.core import serializers
import json
from django.contrib.auth import (authenticate, get_user_model)
from django.contrib.auth.decorators import login_required

User = get_user_model()
@login_required(login_url='account:login')
def home(request):
    
    # user_id = request.user.id
    # this_user = User.objects.get(id=user_id)
    # my_trips = this_user.have_joined.all()
    # all_trips = Destination.objects.exclude(users_on_trip=user_id)

    # context = {
    #     'all_trips': all_trips,
    #     'my_trips': my_trips,
    # }
    return render(request, 'travel_buddy/dashboard.html',)