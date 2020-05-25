from __future__ import unicode_literals

from django.conf import settings

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TransportLocation(models.Model):
    author = models.ForeignKey( User, related_name="authorlocation", on_delete=models.CASCADE)
    name = models.CharField(max_length=50 , default='thisloco')

    locationname = models.CharField( max_length=100, null=False)
    street  = models.CharField( max_length=500, null=True)
    streetnr = models.CharField( max_length=500, null=True)
    zip     = models.CharField( max_length=500, null=True)
    city    = models.CharField( max_length=500, null=True)
    country = models.CharField( max_length=500, null=True)
    geoLat  = models.DecimalField( max_digits=19, decimal_places=10, default=0, null=True) ## muss sein ist die Quell
    geoLon  = models.DecimalField( max_digits=19, decimal_places=10, default=0, null=True)

    lastused = models.DateTimeField(auto_now_add=True)

class Transport(models.Model):

    name = models.CharField(max_length=50, default='thistrans')
    active = models.BooleanField(default=1)

    # person starts transport
    author = models.ForeignKey(User, related_name="writer", null=True, on_delete=models.CASCADE)

    # person having the transport in its hands
    currentHolder = models.ForeignKey(User, related_name="holder", null=True, on_delete=models.CASCADE)            ## FK

    # recipient is the person who closes the transport, 
    recipient   = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    # times of your live
    begin           = models.DateTimeField(auto_now_add=True)
    lasttouched     = models.DateTimeField(auto_now_add=True)

    # metadata 
    contentClass = models.CharField(max_length=500, default='' )
    contentDescription = models.CharField(max_length=100, null=True)
    contentSize = models.CharField(max_length=100, null=True)
    contentWeight = models.CharField(max_length=100, null=True)


    def __unicode__(self):
        return self.name

class TransportPass(models.Model):

    transport   = models.ForeignKey( Transport , on_delete=models.CASCADE)
    touched     = models.DateTimeField(auto_now_add=True)

    # person having the transport in its hands and where this person was 
    newcurrentHolder = models.ForeignKey(User, related_name="newholder", null=True, on_delete=models.CASCADE)
    points        = models.PositiveSmallIntegerField(null=True, default=1)


    location        = models.CharField(max_length=100, null=True)
    locationLat     = models.CharField(max_length=100, null=True)
    locationLon     = models.CharField(max_length=100, null=True)
    logdump         = models.CharField(max_length=1000, null=True)

class TransportUserLocation(models.Model):
    # a person can only be at one place, but many persons at one place
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    location =  models.ForeignKey(TransportLocation , on_delete=models.CASCADE)
    
    changed =   models.DateTimeField(auto_now_add=True)


class TransportUserGetFet(models.Model):

    GETORFETCH = (
        ('sleeping','Sleeping'),
        ('carrying','Carrying'),
        ('hubbing', 'Hubbing'),
        ('flooding','only Flooding'),
        ('grabbing','only Grabbing'),
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    getfet = models.CharField(max_length=8, choices=GETORFETCH , default='grabbing')
    changed = models.DateTimeField(auto_now_add=True)
