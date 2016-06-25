function fillText(data) {

    $( '#text' ).html('')
        .scrollTop();

    var all = data.allLocations;

    // clustered cities?
    if ( all ) {
        for ( var i = 0; i < all.length; i++ ) {
            if ( i ) {
                const ii = i
                var newP = $('<h5></h5>');
                newP.html("gehe zu: " + all[ii].location + " <small>" + all[ii].n + "</small>");
                newP.css("cursor", "pointer");
                newP.click( function() {
                    var headingId = "#" + escape(all[ii].location).replace('%','');
                    console.log(this)
                    $('#text').scrollTop($('#text').scrollTop() + $(headingId).position().top);
                });
                newP.insertAfter("#text h2:first-child");
            }
            $( "#text" ).append('<h2 id=' + escape(all[i].location).replace('%','') + '>' + all[i].location + ' <small>' + all[i].n +'</small></h2>');
            fillIncidents( all[i].incidents );
        }
    } else {
        $( "#text" ).append('<h2>' + data.location + ' <small>' + data.n +'</small></h2>');
        fillIncidents( data.incidents )
    }
};

function fillIncidents( incidents ) {
    for (var i = incidents.length - 1; i >= 0; i--) {
        var mydate = new Date(incidents[i].date);
        $( "#text" ).append( "<p><small>" + mydate.toLocaleDateString('de-DE') + "</small></p>" );
        $( "#text" ).append( "<p>" + incidents[i].text + "</p>" );
        $( "#text" ).append( "<p><small>Quelle: " + incidents[i].source + "</small></p><hr>" );
    }
}

function sumCities(cities) {
    var total = 0;
    var allLocations = [];
    var bestN = -1;
    var bestLocation;

    $.each(cities, function(i, city) {

        if ( city.allLocations ) {
            allLocations = allLocations.concat(city.allLocations);

            var tempN = city.n;

            // Hack: It's not correct. ¯\_(ツ)_/¯ 
            if ( tempN > bestN ) {
                bestN = tempN;
                bestLocation = city.location;
            }

            total += tempN;
        } else {
            allLocations.push(city);
            total += city.n;

            if ( city.n > bestN ) {
                bestN = city.n;
                bestLocation = city.location;
            }
        }
    });

    return {location: bestLocation, n: total, allLocations: allLocations };
};

$(function() {
    // console.log('test');
    var mobile = false
    if( $(window).width() <= 992 ){
        mobile = true;

        $(' #infoText').append("<i>In der mobilen Ansicht wurde die Anzahl der dargestellen Orte reduziert</i>");
    }

    // initialize tooltips
    $.fn.qtip.defaults.style.classes = 'qtip-light';
    $.fn.qtip.defaults.style.def = false;

    var map = kartograph.map('#map');
    map.loadMap('map.svg', function() {

        map.addLayer('roads', {
            styles: {
                stroke: 'grey',
                fill: 'white',
            }
        });

        $.ajax({
            url: 'cities.json',
            dataType: 'json',
            success: function(cities) {
                console.log(kartograph);
                
                var scale = kartograph.scale.sqrt(cities.concat([{ n: 0 }]), 'n').range([2, 18]);

                if( mobile ){
                    cities = cities.filter(function (x) {return x.n > 11})
                }

                map.addSymbols({
                    type: kartograph.LabeledBubble,
                    data: cities,
                    location: function(city) {
                        return [city.lng, city.lat];
                    },
                    radius: function(city) {
                        return scale(city.n);
                    },
                    title: function(city){
                        if (city.location == 'Magdeburg')
                            return city.location;
                         if (city.location == 'Halle')
                            return city.location;
                        else return null;
                    },
                    labelattrs: { 'font-size': 8, 'fill': 'black' },
                    center: false,

                    tooltip: function(city) {

                        if (city.allLocations) {
                            return '<h3>' + city.location + '<small> +' + (city.allLocations.length - 1) + '</small>' + '</h3>' + city.n +' Vorfälle'; 
                        }
                        return '<h3>'+city.location+'</h3>'+city.n+' Vorfälle';
                    },
                    click: function(data, path, event) {
                        fillText(data);

                        if( data.allLocations )
                            var loc = data.allLocations[0].location;
                        else
                            var loc = data.location


                        path.path.attr("fill","black");


                        if( $(window).width() <= 992 ){
                            $('html, body').animate({
                                scrollTop: $("#text").offset().top
                            }, 2000);
                            $('#return-to-top').fadeIn(200);    // Fade in the arrow

                        }
                    },
                    clustering: 'noverlap',
                    clusteringOpts: {
                        tolerance: 0.0,
                        maxRatio: 1
                    },
                    aggregate: sumCities,
                    sortBy: 'radius desc'
                });

                if( mobile ){
                    $('[data-hasqtip]').qtip('hide').qtip('disable');
                }
            }
        });
    });

    // scroll back to map in mobile view 
    $('#return-to-top').click(function() {      // When arrow is clicked
        $('#return-to-top').fadeOut(200);
        $('body,html').animate({
            scrollTop : $("#map").offset().top                // Scroll to top of body
        }, 500);
    });
});


