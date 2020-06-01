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


from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static




from django.urls import path, re_path
from . import views


app_name = 'kohrsupply'
urlpatterns = [

    path('', views.transport_list, name='transport_list'),

    re_path(r'^accounts/profile/$', RedirectView.as_view(url='/')), ## Workaround to get to start after login

    re_path('^transport/(?P<pk>\d+)/$', views.transport, name='transport'),

    re_path(r'^transport/edit/$', views.transport_edit, name='transport_new'),

    re_path(r'^transport/edit/(?P<pk>\d+)/$', views.transport_edit, name='transport_edit'),

    path('^', include('django.contrib.auth.urls')),
    re_path(r'^signup$', views.signup, name='signup'),
    re_path(r'^logout$', views.logout, name='logout' ),
    re_path(r'^password_reset$', views.password_reset, name='password_reset'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset, name='password_reset_confirm'),
    re_path(r'^password_reset/done/$', views.password_reset, name='password_reset_done'),
    re_path(r'^password_reset/complete/$', views.password_reset, name='password_reset_complete'),


    re_path(r'^location/(?P<pk>\d+)/$', views.location, name='location'),
    re_path(r'^location/$', views.location_edit, name='location_edit'),
    re_path(r'^location/edit/(?P<pk>\d+)/$', views.location_edit, name='location_edit'),
    path('locations', views.locations, name='locations'),

    re_path(r'^carriers/$', views.carriers, name='carriers'),
    re_path(r'^carrier/(?P<pk>\d+)/$', views.carrier, name='carrier'),


    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^about/(?P<pk>[0-9A-Za-z]+)/$', views.about, name='about'),




    re_path(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#~ ] + static('/static/', document_root='/home/kohr/kohrsupply/kohrsupply/static/')
