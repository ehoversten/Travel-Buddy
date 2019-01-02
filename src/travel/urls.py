
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include(('apps.accounts.urls', 'account'), namespace='account')),
    url(r'^travel/', include(('apps.travel_buddy.urls', 'travel'), namespace='travel')),
    url(r'^admin/', admin.site.urls),
]
