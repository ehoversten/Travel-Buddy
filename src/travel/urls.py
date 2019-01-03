from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^', include(('apps.accounts.urls', 'account'), namespace='account')),
    url(r'^travel/', include(('apps.travel_buddy.urls', 'travel'), namespace='travel')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]



if settings.DEBUG:  # If it is in debug mode
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

