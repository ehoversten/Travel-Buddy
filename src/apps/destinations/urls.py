from django.conf.urls import url
from .views import (
    HomeView,
    AddDestinationFormView,
    DestinationDetailSlugView,
    UpdateDestinationView
)

urlpatterns = [
    url(r'^dashboard$', HomeView.as_view(), name='home'),
    url(r'^destination/add$', AddDestinationFormView.as_view(), name='add_trip'),
    url(r'^destination/update/$', UpdateDestinationView, name='destination_update'),
    # url(r'^destination/update/$', UpdateDestinationView.as_view(), name='destination_update'),
    url(r'^destination/(?P<slug>[\w-]+)/$', DestinationDetailSlugView.as_view(), name='detail'),

]
