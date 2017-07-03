from django import forms
from .models import Transport, TransportUserGetFet, TransportLocation
from django.contrib.auth.models import User


class CreateTransport(forms.ModelForm):

    contentClasses = (
            ("nonfood", "Non food"),
            ("people", "People"),
            ("food", "Food"),
            ("warmfood", "Warm food"),
            ("chilledfood", "chilled food"),
            ("deepfrozenfood", "deep-frozen food"),
            ("laundry", "Laundry"),
            ("garbage", "Garbage"),
    )

    holdername =            forms.CharField(    widget=forms.TextInput(attrs={'class': 'users'}))
    recipientname =         forms.CharField(    widget=forms.TextInput(attrs={'class': 'users'}))

    contentDescription =    forms.CharField(    widget=forms.TextInput, required=False,)
    contentClass =          forms.ChoiceField(  widget=forms.Select, choices=contentClasses, required=True,)
    contentSize =           forms.CharField(    widget=forms.TextInput, required=False,)
    contentWeight =         forms.CharField(    widget=forms.TextInput, required=False,)

    class Meta:
        model = Transport
        fields = ('recipientname',  'contentDescription', 'contentClass', 'contentSize', 'contentWeight' )

class UserState(forms.ModelForm):
    class Meta:
        model = TransportUserGetFet
        fields = ( 'getfet', )

class TransportUserLocationEdit(forms.ModelForm):

    street =           forms.CharField(    widget=forms.TextInput, required=False,)
    streetnr =           forms.CharField(    widget=forms.TextInput, required=False,)
    zip =           forms.CharField(    widget=forms.TextInput, required=False,)
    city =           forms.CharField(    widget=forms.TextInput, required=False,)
    country =           forms.CharField(    widget=forms.TextInput, required=False,)
    
    # use plain input to get no comma seperatoer hassle
    geoLat =           forms.CharField(    widget=forms.TextInput, required=False,)
    geoLon =           forms.CharField(    widget=forms.TextInput, required=False,)


    class Meta:
        model = TransportLocation
        fields = ('locationname','street','streetnr','zip','city','country','geoLat', 'geoLon',)
