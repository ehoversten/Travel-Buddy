from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic import CreateView

from .models import *
from .forms import LoginForm

"""
def index(request):
    # User.objects.all().delete()
    # Destination.objects.all().delete()
    return render(request, 'travel_buddy/index.html')
"""

"""Can replace index function."""
class IndexView(TemplateView):
    template_name = "travel_buddy/index.html"
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["form"] = LoginForm()
        return context


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


"""Can replace home function."""
class HomeView(TemplateView):
    template_name = "travel_buddy/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        this_user_id = self.request.session['id']
        this_user = User.objects.get(id=int(this_user_id))
        my_trips = this_user.have_joined.all()
        all_trips = Destination.objects.exclude(users_on_trip=this_user_id)

        context["all_trips"] = all_trips
        context["my_trips"] = my_trips
        return context

"""
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
"""

"""Can replace show function."""
class ShowView(TemplateView):
    template_name = 'travel_buddy/show.html'

    def get_context_data(self, **kwargs):
        context = super(ShowView, self).get_context_data(**kwargs)
        url = self.request.path_info
        url = int(url.replace("/travels/destination/", ""))
        this_dest = Destination.objects.get(id=url)
        other_users = this_dest.users_on_trip.exclude(id=this_dest.planner_id)
        context["destination"] = this_dest
        context["others"] = other_users
        return context



def process_reg(request):
    results = User.objects.reg_validator(request.POST)

    if results[0]:
        # Do not understand this code completly. User info stores in session automatically wtih django.  Also, do think you think it would be good to redirect to index to login in in any case?
        request.session['id'] = results[1].id
        request.session['name'] = results[1].name
        print("reg success")
        return redirect('/main')
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


"""Can replace index function."""
class AddTripView(TemplateView):
    template_name = "travel_buddy/add.html"


def join_trip(request, trip_id):
    user_id = request.session['id']
    user_to_join = User.objects.get(id=user_id)
    this_trip = Destination.objects.get(id=trip_id)
    user_to_join.have_joined.add(this_trip)
    return redirect('/travels')


def logout(request):
    request.session.clear()
    return redirect('/main')
