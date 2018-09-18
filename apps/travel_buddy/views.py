from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    # User.objects.all().delete()
    # Destination.objects.all().delete()
    return render(request, 'travel_buddy/index.html')

def home(request):
    this_user_id = request.session['id']
    this_user = User.objects.get(id=int(this_user_id))
    # this_user.have_joined.all()
    # my_trips = Destination.objects.filter(planner=this_user)
    my_trips = this_user.have_joined.all()
    # all_trips = Destination.objects.exclude(planner=this_user)
    all_trips = Destination.objects.exclude(users_on_trip=this_user_id)

    context = {
        'all_trips' : all_trips,
        'my_trips' : my_trips,
    }
    return render(request, 'travel_buddy/home.html', context)


def show(request, id):
# --- SET variable to retrieve the OBJECT tied to the recieved ID ---
    this_dest = Destination.objects.get(id=id)
# *** TEST ***
    print("-"*25)
    print('Destination OBJECT contains: ', this_dest.location)
    print("-"*25)
    other_users = this_dest.users_on_trip.exclude(id=this_dest.planner_id)
    print("-"*25)
    print('Other_users OBJECT contains: ', other_users)
    print("-"*25)

    # all_trips = Destination.objects.exclude(planner=this_user)

# --- Assign our VARIABLE within our CONTEXT DICTIONARY for passing to our views ---
    context = {
        'destination' : this_dest,
        'others' : other_users,
    }
# --- Pass our OBJECT in our context to our HTML view
    return render(request, 'travel_buddy/show.html', context)


def process_reg(request):
    results = User.objects.reg_validator(request.POST)

    if results[0]:
        request.session['id'] = results[1].id
        request.session['name'] = results[1].name
        return redirect('/travels')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='register')
        return redirect('/main')

def process_login(request):
    results = User.objects.loginValidator(request.POST)

    if results[0]:
        request.session['id'] = results[1].id
        request.session['name'] = results[1].name
        return redirect('/travels')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='login')
        return redirect('/main')

    # return redirect('/main')


def process_add(request):
# --- Pass in the request.POST **and** SESSION
    results = Destination.objects.dest_validator(request.POST, int(request.session['id']))
    print("*"*25)
    print('RESULTS: ', results)
    print("*"*25)

    if results[0]:

        return redirect('/travels')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error, extra_tags='register')
        return redirect('/travels/add')
    return redirect('/')

def add_trip(request):
    return render(request, 'travel_buddy/add.html')

def join_trip(request, trip_id):
    user_id = request.session['id']
    # print("*"*25)
    # print('user_id: ', user_id)
    # print('\n')
    user_to_join = User.objects.get(id=user_id)
    # print("*"*25)
    # print('user_to_join: ', user_to_join.name)
    # print('\n')
    this_trip = Destination.objects.get(id=trip_id)
    # print("*"*25)
    # print('This TRIP object name: ', this_trip.location)
    # print('\n')
    user_to_join.have_joined.add(this_trip)
    # this_trip.users.add(user_to_join)
    return redirect('/travels')


def logout(request):
    request.session.clear()
    return redirect('/main')
