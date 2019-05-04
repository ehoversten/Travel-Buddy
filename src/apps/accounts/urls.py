from django.conf.urls import url
from .views import (
    register_view,
    LoginFormView
)

urlpatterns = [
    url(r'^$', LoginFormView.as_view(), name='login'),
    # url(r'^$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
]
