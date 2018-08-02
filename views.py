import json
import datetime
import markdown

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.db.models import Sum

from django.shortcuts import render_to_response, render, redirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset



from django.utils import timezone
from django.utils.safestring import SafeString
from django.shortcuts import get_object_or_404

from math import radians, cos, sin, asin, sqrt
from json import dumps, loads, JSONEncoder, JSONDecoder

from .models import Transport, TransportPass, TransportLocation, TransportUserGetFet, TransportUserLocation
from .forms import CreateTransport , TransportUserLocationEdit

###################

filterargsLocationUser = { }

def transport_list(request):

    class geosearch(object):
        pass
    userLocationsusers = latrange = lonrange = ''
    listuserLocationsusers = []
    filterargsTransport = { 'active' : True } 


    # /?class=nonfood
    if request.GET.get('class')  :
        classes = request.GET['class']
        filterargsTransport.update ( { 'contentClass' : classes } )

    filterargsTransport.update ( { 'currentHolder__in' : usersGetFetActive() } )

    # reset all filters
    if request.GET.get('all')  :
        filterargsTransport = { }


    # /?lat=48.1&lon=11.6&wide=6
    if request.GET.get('lat') and request.GET.get('lon') :

        lat = float( request.GET['lat'] )
        lon = float( request.GET['lon'] )
        wide = 0.17

        if request.GET.get('wide') :
            wide = float( request.GET['wide'] ) 

        transportscount = 0 # to while at least 1 time calling latlonrange 
        while transportscount == 0 :
            latlonrange(lat, lon, wide , geosearch, filterargsTransport, filterargsLocationUser )

            # # zoomout
            # stretch your requested area until you get at least one trensport 
            if request.GET.get('zoomout') :
                transportscount = Transport.objects.filter( **filterargsTransport ).count()
                wide = wide + 1
            else :
                break

    transports = Transport.objects.filter( **filterargsTransport ).order_by('-id').select_related()[:100]

    buildTransports( transports )

    return render(request, 'kohrsupply/transports.html',  { 'transports': transports , 'userLocationsusers' : usersWillingTakover ( ) , 'geosearch' : geosearch  })


def usersGetFetActive ( ) :
    # get users with getfet: hubbing, flooding (to hide carrying, sleeping and grabbing)
    userGetfetusers = TransportUserGetFet.objects.filter( Q(getfet = 'hubbing' ) | Q(getfet = 'flooding' ) )
    userGetfetusersusers = list( userGetfetusers.values_list('user',  flat=True ) )

    return userGetfetusersusers


def usersWillingTakover (  ) :

    filterargsLocationUser.update ( user_id__in= usersGetFetActive()  )
    userLocationsusers = TransportUserLocation.objects.filter(  **filterargsLocationUser  )

    return userLocationsusers


def latlonrange( lat, lon, wide, geosearch, filterargsTransport, filterargsLocationUser ):

    wide = wide / 100 # avoid dots  in url
    latrange = ( lat - wide , lat + wide )
    lonrange = ( lon - wide , lon + wide )

    geosearch.lat = lat
    geosearch.lon = lon
    geosearch.wide = wide
    geosearch.latrange = latrange
    geosearch.lonrange = lonrange

    # get users sitting in location search area, to show their transport and themselve
    # TODO doublicate query
    userLocationsusers = TransportUserLocation.objects.filter( location__geoLat__range = latrange ).filter( location__geoLon__range = lonrange )
    listuserLocationsusers = list( userLocationsusers.values_list('user',  flat=True ) )
    filterargsTransport.update ( { 'currentHolder__in' : listuserLocationsusers } )

    filterargsLocationUser.update ( { 'location__geoLat__range' : latrange, 'location__geoLon__range' : lonrange } )


def transport(request, pk ):

    transport = get_object_or_404(Transport, pk=pk)

    transportPasses = TransportPass.objects.filter( transport = transport )

    if request.POST.get('transport') :
        if transport.currentHolder == request.user :
            messages.warning(request, 'You own this transport already')

        if request.user.is_authenticated  :
            transportTake( transport, request, 1 )
        else :
            messages.warning(request, 'To take a transport, please login')

    if request.POST.get('close') and transport.recipient_id == request.user.id :

        transport.currentHolder = request.user
        transport.active = False
        transport.getfet = 'close'
        transport.save()

    buildTransport( transport )

    return render(request, 'kohrsupply/transport.html', {         'transport': transport, 'transportPasses' : transportPasses   })


@login_required
def transport_edit(request, pk=None):

    if pk:
        transport = get_object_or_404(Transport, pk=pk)

        if transport.author != request.user and transport.recipient != request.user and request.user.is_superuser == False :
            return render(request, 'kohrsupply/transports.html' )

    else:
        transport = Transport()

    form = CreateTransport(request.POST or None, instance=transport)
    if request.POST and form.is_valid() :

        # todo write username from id in field
        transport.currentHolder = User.objects.get( username__iexact = request.POST['holdername'] )
        transport.recipient = User.objects.get( username__iexact = request.POST['recipientname'] )

        if pk == None : 
            transportTake( transport, request, 0 )
            transport.author_id = request.user.id
        form.save()

        # Save was successful, so redirect this transport
        return redirect('transport', pk= transport.id )

    return render(request, 'kohrsupply/transport_edit.html' , {'form': form , 'transportid' : pk })

def location(request, pk=None):

    thisLocation                = TransportLocation.objects.get(pk=pk)

    ## every user at this location  
    locationUserTransports      = TransportUserLocation.objects.filter( location = thisLocation ).order_by( '-id' ) 

    ## every transport at this locattion
    currentTransports = []
    recipientTransports = []

    for locationUserTransport in locationUserTransports :
        currentTransports.append(   Transport.objects.filter( active = True ).filter( currentHolder = locationUserTransport.user ) )
        recipientTransports.append( Transport.objects.filter( active = True ).filter( recipient =     locationUserTransport.user ) )

    if request.POST.get('delete') and request.user == thisLocation.author :
        u = thisLocation .delete()

    return render(request, 'kohrsupply/location.html', { 'location' : thisLocation , 'currentTransports' : currentTransports , 'recipientTransports' : recipientTransports , 'locationUserTransports' : locationUserTransports } )

def location_edit (request, pk=None):

    # show past locations

    if pk :
        transportuserlocation = TransportLocation.objects.get(pk=pk)
    else :
        transportuserlocation = TransportLocation()

    form = TransportUserLocationEdit(request.POST or None, instance=transportuserlocation)

    if request.POST and form.is_valid():

        # store used location in users location list
        transportuserlocation.author = request.user

        form.save()

        return redirect('location', pk= transportuserlocation.id )
    
    return render(request, 'kohrsupply/location_edit.html',  {'form': form  })
    
    
def locations(request):

    transportlocations = TransportLocation.objects.order_by('-id')[:100]

    return render(request, 'kohrsupply/locations.html',  {'transportlocationlist' : transportlocations })

##### includes
#~ @login_required
def transportTake (  transport, request, points ) :
 
    transportPass = TransportPass()
    try :
        currentHolderLocation = TransportUserLocation.objects.get( user = request.user )
    except ObjectDoesNotExist :
        return

    transport.currentHolder     = request.user
    transport.lasttouched       =  datetime.datetime.now()
    transport.save()

    transportPass.transport = transport
    transportPass.newcurrentHolder = request.user
    transportPass.points = points
    transportPass.logdump = transport.contentDescription
    transportPass.location = currentHolderLocation.location.locationname
    transportPass.locationLat = currentHolderLocation.location.geoLat
    transportPass.locationLon = currentHolderLocation.location.geoLon
    transportPass.save()


def buildTransports( transports ) :
    transportz = []
    for transport in transports : 
        buildTransport( transport )
        transportz.append( transport )

    transports = transportz
    return transports


def buildTransport( transport ) :

    # location of current Holder
    try :
        transport.currentLocation = TransportUserLocation.objects.get( user = transport.currentHolder ).location
    except ObjectDoesNotExist : #  avoid current Holder with no location
        return

    # points of current Holder
    try :
        transport.currentHolderPoints = TransportPass.objects.filter( newcurrentHolder = transport.currentHolder ).aggregate(summa = Sum('points'))
    except ObjectDoesNotExist : #  avoid current Holder with no points
        return

    # getfet of current Holder
    try : 
        transport.getfet   = TransportUserGetFet.objects.get(   user = transport.currentHolder ).getfet

    except ObjectDoesNotExist : #  avoid user with no getfet 
        return


    # location of recipient
    try :
        transport.recipientLocation     = TransportUserLocation.objects.get( user = transport.recipient ).location
    except ObjectDoesNotExist : #  avoid recipient with no location
        return

    # points of recipient
    try :
        transport.recipientPoints     = TransportPass.objects.filter( newcurrentHolder = transport.recipient ).aggregate(summa = Sum('points'))
    except ObjectDoesNotExist : #  avoid recipient with no point
        return

    # getfet of recipient
    try : 
        transport.recipientgetfet   = TransportUserGetFet.objects.get(   user = transport.recipient ).getfet

    except ObjectDoesNotExist : #  avoid user with no getfet 
        return


    transport.distance2target       = haversine( transport.currentLocation , transport.recipientLocation )


def haversine( current, recipient ):
    # from http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    # TODO https://pypi.python.org/pypi/geopy Measuring Distance

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [current.geoLon, current.geoLat, recipient.geoLon, recipient.geoLat])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return round( c * r, 2 )


#####

def carrier(request, pk = None):

    carrier = User.objects.get( pk = pk )

    # TODO split in recipient and holder
    transports = Transport.objects.filter( active = True ).filter( Q(currentHolder = carrier ) | Q(recipient = carrier ) ).order_by('-id')[:100]

    buildTransports(transports)

    return render(request, 'kohrsupply/carrier.html',  {'carrier' : carrier , 'transports' : transports } )

def carriers(request, pk = None):
    filterargs = { }

    if request.GET.get('term') :
        filterargs.update ( username__contains = request.GET.get('term') )

    carriers = User.objects.filter( **filterargs )[:100]

    # TODO get more then only names, also location etc
    if ( request.GET.get('format') == "json") : # /carriers/?format=json&term=e
        carriernames = []
        for carrier in carriers :
            carriernames.append( carrier.username )

        return JsonResponse( carriernames , safe=False) 


    return render(request, 'kohrsupply/carriers.html',  {'carriers' : carriers } )



# http://stackoverflow.com/questions/10372877/how-to-create-a-user-in-django#23482284
def signup(request):

    #~ if request.POST["username"] :
    if request.POST :
        #~ userName = request.REQUEST.get('username', None)
        userName = request.POST['username']
        userPass = request.POST['password']
        userMail = request.POST['email']

    # TODO: check if already existed
        if userName and userPass and userMail:
            user = User.objects.create_user(username= userName , email= userMail, password= userPass )
            #~ if created:
              # user was created
              # set the password here
            return render(request,'registration/done.html')
           #~ else:
              # user was retrieved
        #~ else:
           # request was empty
    
    return render(request,'registration/signup.html')

def change_password(request):
    template_response = views.password_change(request)
    # Do something with `template_response`
    return template_response


def password_reset(request):
    if request.method == 'POST':
        return password_reset(request, 
            from_email=request.POST.get('email'))
    else:
        return render(request,'registration/password_reset_form.html')
    

def about(request, pk='index'):
    mdfile = 'kohrsupply/about/' + pk + '.md'
    contentmd = open( mdfile ).read(10000).decode("utf-8")
    content = markdown.markdown( contentmd ) 
    return render(request,'kohrsupply/about.html', { 'content': content , })
