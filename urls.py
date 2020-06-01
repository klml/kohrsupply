"""kohrsupply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include

from . import views

from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static



app_name = 'kohrsupply'
urlpatterns = [

    url(r'^$', views.transport_list, name='transport_list'),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/')), ## Workaround to get to start after login

    url(r'^transport/(?P<pk>\d+)/$', views.transport, name='transport'),
    url(r'^transport/edit/$', views.transport_edit, name='transport_new'),

    url(r'^transport/edit/(?P<pk>\d+)/$', views.transport_edit, name='transport_edit'),

    url('^', include('django.contrib.auth.urls')),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout$', views.logout, name='logout' ),
    url(r'^password_reset$', views.password_reset, name='password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset, name='password_reset_confirm'),
    url(r'^password_reset/done/$', views.password_reset, name='password_reset_done'),
    url(r'^password_reset/complete/$', views.password_reset, name='password_reset_complete'),


    url(r'^location/(?P<pk>\d+)/$', views.location, name='location'),
    url(r'^location/$', views.location_edit, name='location_edit'),
    url(r'^location/edit/(?P<pk>\d+)/$', views.location_edit, name='location_edit'),
    url(r'^locations$', views.locations, name='locations'),

    url(r'^carriers/$', views.carriers, name='carriers'),
    url(r'^carrier/(?P<pk>\d+)/$', views.carrier, name='carrier'),


    url(r'^about/$', views.about, name='about'),
    url(r'^about/(?P<pk>[0-9A-Za-z]+)/$', views.about, name='about'),

    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#~ ] + static('/static/', document_root='/home/kohr/kohrsupply/kohrsupply/static/')
