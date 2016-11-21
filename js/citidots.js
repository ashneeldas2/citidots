var filename = '../data/data.json';

$.getJSON(filename, function(json) {
    var bikes = json;
});

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: {lat: 40.719517, lng: -73.982786},
        mapTypeId: 'terrain'
    });

    var activeBikes = [];
    var ticks = 0;

    window.setInterval(function(){

        for (var bikeid in bikes){
            if (bikes[bikeid].starttime == ticks){
                activeBikes.push( new google.maps.Circle({
                    strokeColor: '#39A2E1',
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillColor: '#39A2E1',
                    fillOpacity: 1,
                    map: map,
                    center: {lat: bikes[bikeid].startLoc[0], lng: bikes[bikeid].startLoc[1]},
                    radius: 20,
                    startLoc: {lat: bikes[bikeid].startLoc[0], lng: bikes[bikeid].startLoc[1]},
                    endLoc: {lat: bikes[bikeid].endLoc[0], lng: bikes[bikeid].endLoc[1]},
                    angle: 40*(Math.PI / 180),
                    v: 0.0001,
                    hasTurned: false,
                }));
            }
        }
        activeBikes.forEach(function(bike) {
            var sX = bike.startLoc['lng'];
            var sY = bike.startLoc['lng'];
            var eX = bike.endLoc['lng'];
            var eY = bike.endLoc['lat'];

            var d = Math.sqrt(Math.pow((eX-sX),2) + Math.pow((eY-sY), 2));
            var p = bike.getCenter();
            var m = p.lng();
            var g = p.lat();

            dY = eY - sY;
            dX = eX - sX;
            theta = arctan(dY/dX);

            var north = eX > sX;
            var south = !north;
            var east = eY > sY;
            var west = !east;

            m = p.lng() + bike.v*(Math.sin(bike.angle));
            g = p.lat() + bike.v*(Math.cos(bike.angle));


            bike.setCenter(new google.maps.LatLng(g,m));
            bike.setRadius(10);

            });
            ticks++;
    }, 2);
}
