# The context processor function
# http://matthewphiong.com/django-global-template-variable

import datetime
from django.core.exceptions import ObjectDoesNotExist

from .models import Transport, TransportLocation, TransportUserGetFet, TransportUserLocation
from .forms import UserState

def userstate(request):

    # get users current getfet state and form to change it
    if request.user.id :

        # must try if user has not set state yet... 
        try:
            userstate = TransportUserGetFet.objects.get( user = request.user.id )
        except ObjectDoesNotExist:
            userstate = TransportUserGetFet()

        userstateform = UserState(request.POST or None, instance=userstate )

        # change users possibility to fetch or hand over transports
        if request.POST.get('getfet') :
            userstate.getfet = request.POST['getfet']
            userstate.user = request.user
            userstate.changed = datetime.datetime.now()
            userstate.save()

        return { 'requestUserStatestate' : userstate.getfet ,  'userstateform' : userstateform }
    # anonymus
    else:
        return { 'requestUserStatestate' : '' ,  'userstateform' : '' , }


def usersLocations(request):

    if request.POST.get('checkin') and request.user:
        try:
            transportuserlocations = TransportUserLocation.objects.get( user = request.user.id )
        except ObjectDoesNotExist :
            transportuserlocations = TransportUserLocation()

        transportlocation = TransportLocation.objects.get( pk = request.POST['checkin'] )

        transportuserlocations.user     = request.user
        transportuserlocations.location = transportlocation
        transportuserlocations.geoLat   = transportlocation.geoLat
        transportuserlocations.geoLon   = transportlocation.geoLon
        transportuserlocations.changed  = datetime.datetime.now()
        
        transportuserlocations.save()

    try:
        usersLocations = TransportUserLocation.objects.get( user = request.user.id )
        return { 'usersLocations': usersLocations , }
    except ObjectDoesNotExist: ## catch anonymus and user without location
        return { 'usersLocations': '' , }
