
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.article_list, name='list'),
    url(r'^', include('apps.travel_buddy.urls')),
]
