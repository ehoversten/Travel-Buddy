from django.conf.urls import url
from django.urls import path

from . import views
from .views import IndexView, HomeView, ShowView, AddTripView

urlpatterns = [
    # url(r'^$', views.index),
    # url(r'^main$', views.index),
    # url(r'^travels$', views.home),
    url(r'^travels/process_reg$', views.process_reg),
    url(r'^travels/process_login$', views.process_login),
    url(r'^travels/process_add$', views.process_add),
    url(r'^process_add$', views.process_add),

    # url(r'^travels/add$', views.add_trip),
    url(r'^travels/add_trip$', views.add_trip),
    url(r'^travels/logout$', views.logout),
    url(r'^logout$', views.logout),

    # url(r'^travels/(?P<id>\d+)$', views.show),
    # url(r'^travels/destination/(?P<id>\d+)$', views.show),
    # url(r'^travels/join_trip$', views.join_trip),
    url(r'^travels/join_trip/(?P<trip_id>\d+)$', views.join_trip),

    path("", IndexView.as_view()),
    path("main", IndexView.as_view()),
    path("travels", HomeView.as_view()), 
    path("travels/destination/<str:pk>", ShowView.as_view()),
    path("travels/add", AddTripView.as_view()), 

]
