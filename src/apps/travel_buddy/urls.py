from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^dashboard$', views.home, name='home'),
    #     # Login and add process
    # url(r'^travels/process_reg$', views.process_reg),
    # url(r'^travels/process_login$', views.process_login),
    # url(r'^travels/process_add$', views.process_add),
    # url(r'^process_add$', views.process_add),
    #     # Remove it from logged in users plans
    # url(r'^travels/leave_trip/(?P<trip_id>\d+)$', views.leave_trip),

    # url(r'^travels/add$', views.add_trip),
    # url(r'^travels/add_trip$', views.add_trip),
    # url(r'^travels/logout$', views.logout),
    # url(r'^logout$', views.logout),

    # url(r'^travels/destination/(?P<id>\d+)$', views.show),
    # url(r'^travels/join_trip/(?P<trip_id>\d+)$', views.join_trip),
    # url(r'^travels/remove_trip/(?P<trip_id>\d+)$', views.delete_trip),

    # # AJAX ROUTES
    # url(r'^travels/ajax$', views.ajax_testing),
    # url(r'^travels/all_html$', views.all_html),
    # url(r'^travels/all.json$', views.all_json),
    # url(r'^all.json$', views.all_json),
    # url(r'^all.html$', views.all_html),
    # url(r'^create$', views.create)



    # Deprecated Routes
    # url(r'^$', views.trip_log_reg), ## Register
    # url(r'^main$', views.trip_log_reg), ##login

]
