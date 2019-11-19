var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

var TectonicPlatesUrl = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_plates.json"

d3.json(queryUrl, function(data) {
  createFeatures(data.features);
});

function createFeatures(earthquakeData) {       

  var earthquakes = L.geoJson(earthquakeData, {
    onEachFeature: function (feature, layer){
      layer.bindPopup("<h3>" + feature.properties.place + "<br> Magnitude: " + feature.properties.mag +
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>")


    },
    pointToLayer: function (feature, latlng) {
      return new L.circle(latlng,
        {radius: getRadius(feature.properties.mag),
          fillColor: getColor(feature.properties.mag),
          fillOpacity: .7,
          stroke: true,
          color: "black",
          weight: .5
      })
    }
  });

  createMap(earthquakes)
}

function createMap(earthquakes) {

  var satelliteMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?"+
    "access_token=pk.eyJ1IjoibWFya21jY3VlIiwiYSI6ImNqbGg4eGRxZzFmczkzd2xxbDZpd2dxOHQifQ.fdKoHJFhD3cWL0zs8mHDGw");


  var outdoorMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v9/tiles/256/{z}/{x}/{y}?"+
    "access_token=pk.eyJ1IjoibWFya21jY3VlIiwiYSI6ImNqbGg4eGRxZzFmczkzd2xxbDZpd2dxOHQifQ.fdKoHJFhD3cWL0zs8mHDGw"); 
   

  var lightMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?"+
    "access_token=pk.eyJ1IjoibWFya21jY3VlIiwiYSI6ImNqbGg4eGRxZzFmczkzd2xxbDZpd2dxOHQifQ.fdKoHJFhD3cWL0zs8mHDGw");

  var baseMaps = {
    "Satellite Map": satelliteMap,
    "Outdoor Map": outdoorMap,
    "Grayscale": lightMap
  };
  var tectonicPlates = new L.LayerGroup();

  var overlayMaps = {
    Earthquakes: earthquakes,
    "Tectonic Plates": tectonicPlates
  };
  
  var myMap = L.map("map", {
    center: [
      37.09, -95.71],
    zoom: 5,
    layers: [satelliteMap]
  });

  d3.json(TectonicPlatesUrl, function(plateData) {
      L.geoJson(plateData, {
        color: "green",
        weight: 2
      })
      .addTo(tectonicPlates);
  });

  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);


   var legend = L.control({position: 'bottomright'});

   legend.onAdd = function (myMap) {

     var div = L.DomUtil.create('div', 'info legend'),
               grades = [0, 1, 2, 3, 4, 5],
               labels = [];

     for (var i = 0; i < grades.length; i++) {
         div.innerHTML +=
             '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
             grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
     }
     return div;
   };

   legend.addTo(myMap);
}

function getColor(d) {
  return d > 5 ? 'FF3300' :
    d > 4  ? 'FF6600' :
    d > 3  ? 'FF9900' :
    d > 2  ? 'FFCC00' :
    d > 1   ? 'FFFF00' :
            'FFFF99';
}

function getRadius(value){
  return value*40000
}