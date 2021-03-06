// geolocation

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition( getStreetCityZip );

    } else {
        alert("Geolocation is not supported by this browser.");
    }
    return ;
};
function getStreetCityZip(position) {

    reverseurl = '//nominatim.openstreetmap.org/reverse?format=json&lat=' + position.coords.latitude + '&lon=' + position.coords.longitude ;

    accuracy = Math.round( position.coords.accuracy ) ;

    $('#id_geoLat').val( position.coords.latitude  );
    $('#id_geoLon').val( position.coords.longitude );

    $.getJSON( reverseurl , function( data ) {

        $("#id_locationname").val( data.display_name.split(',')[0] );
        $("#id_street").val( data.address.road );
        $("#id_streetnr").val(  );
        $("#id_zip").val( data.address.postcode );
        $("#id_city").val( data.address.city );
        $("#id_city").val( data.address.village );
        $("#id_country").val( data.address.country );
    });
};
function setmap() {

    var map = L.map('mapid').setView([ 0, 0 ], 2);

    L.tileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var markers = [];
    var pointDist2TargetList = [];
    var pointLogList = [];
    var boundaries = [ ];

    $('.transport').each( function () {
        var pointDescription = $(this).html() ;
        var content = $(this).find('.content').text().trim() ;

        var holderCoordinates       = $(this).find('.holder').find('.coords').text().split(',') ;
        var recipientCoordinates    = $(this).find('.recipient').find('.coords').text().split(',') ;
        var recipientGetFet    = $(this).find('.recipient').find('.carrier small').text() ;

        var holderPoint     = new L.LatLng( holderCoordinates[0].trim() , holderCoordinates[1].trim() );
        var recipientPoint  = new L.LatLng( recipientCoordinates[0].trim(), recipientCoordinates[1].trim() );


        var contentIcon = L.icon({
            iconUrl: '//img.klml.de/devel/ptap/' + content + '_icon__30.png',
            iconAnchor:   [15, 34],
            iconSize:     [30, 32],
        });
        var recipientIcon = L.icon({
            iconUrl: '//img.klml.de/devel/ptap/ptap_' + recipientGetFet + '_trns__30.png',
        iconAnchor:   [15, 15],
        iconSize:     [30, 30],
        });

        var holderMarker        = new L.marker( holderPoint, { icon: contentIcon }  ).addTo(map).bindPopup( pointDescription );
        var recipientMarker     = new L.marker( recipientPoint , { icon: recipientIcon }  ).addTo(map) ;

        boundaries.push( holderMarker ) ;
        boundaries.push( recipientMarker ) ;


        var pointDist2Target = new L.Polyline( [holderPoint , recipientPoint ] , {
            color: '#77AE9A',
            weight: 3,
            opacity: 1,
            smoothFactor: 1
         }).addTo(map);

        // arrow on target
        var arrowHead = L.polylineDecorator(pointDist2Target, {
            patterns: [
                {offset: '100%', repeat: 0, symbol: L.Symbol.arrowHead({pixelSize: 25, polygon: false, headAngle: 40, pathOptions: {stroke: true }})}
            ]
        }).addTo(map);


        // draw logline
        $(this).find('#log').find('.coords').each( function () {
            var logCoordinates = $(this).text().split(',') ;
            var point = new L.LatLng( logCoordinates[0] , logCoordinates[1] );
            pointLogList.push( point )
        });

        var logline = new L.Polyline( pointLogList , {
            color: '#CF763A',
            weight: 3,
            opacity: 1,
            smoothFactor: 1
        });

        logline.addTo(map);

    });


    // user willing to take transports
    var hubbingIcon = L.icon({
        iconUrl: '//img.klml.de/devel/ptap/ptap_hubbing_trns__30.png',
        iconAnchor:   [15, 15],
        iconSize:     [30, 30],
    });

    $.each(userLocationsusers, function(index, value) {
        marker = [ value['lat'] , value['lon'] ] ;
        newmarker = new L.marker( marker, { icon: hubbingIcon } ).addTo(map).bindPopup( index );
    });

    // location detail page
    $('.location').each( function () {
        var locationCoordinates = $(this).find('.coords').text().split(',') ;
        var locationPoint     = new L.LatLng( locationCoordinates[0].trim() , locationCoordinates[1].trim() );
        newmarker = new L.marker( locationPoint, { icon: hubbingIcon } ).addTo(map) ;
        boundaries.push( new L.marker( locationPoint ) );
    });



    var boundariesgroup = L.featureGroup( boundaries ); // only on transports
    map.fitBounds( boundariesgroup.getBounds() , { padding: [27, 27] });

    if ( typeof geosearch != "undefined" ) {
          //~ TODO geosearch.wide faktor
        L.circle([ geosearch.lat , geosearch.lon ], {radius: geosearch.wide * 70000 , fillOpacity: 0.05 , color : "green" } ).addTo(map);
    };


};

function setqrcode() {
    urlwithoutsearch = window.location.origin + window.location.pathname ;
    qrcodeurl = document.getElementById("qrcodeurl");

    if ( qrcodeurl ) {
        var qrcode = new QRCode( qrcodeurl , {
            text: urlwithoutsearch ,
            width: 128,
            height: 128,
            colorDark : "#000000",
            colorLight : "#ffffff",
            correctLevel : QRCode.CorrectLevel.H
        });
    }
};


function getlocal() {
    navigator.geolocation.getCurrentPosition(function(position) {
        link = '/?lat=' + position.coords.latitude + '&lon=' + position.coords.longitude + '&wide=1&zoomout=1' ;
        $('.getlocal').attr( 'href' , link );
    });
};

jQuery(document).ready(function() {

    $('#log').hide();
    $('.log h3').click( function() {
        $('#log').toggle();
    });

    if( typeof user != "undefined" ) {
        $('form.transport_None #id_holdername').val( user.user_name );
    };

    $( "input.users" ).autocomplete({
        source: '/carriers/?format=json',
        minLength: 0
    });

    $( "#setuserstate button" ).hide();
    $( "#setuserstate select" ).change(function() {
        this.form.submit();
    });


    $('#getStreetZipCity').click( function ( event ) {
        getLocation();
    });

    setqrcode();

    getlocal();
    setmap();

});
