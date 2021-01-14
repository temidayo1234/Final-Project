// Creating map object
var myMap = L.map("map", {
  center: [37.4316, -78.6569],
  zoom: 7
});

// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY,
}).addTo(myMap);

var city = [];
var lat = [];
var lon = [];
var CrimeRate = [];

var markers = L.markerClusterGroup();

location_data.forEach(function (data) {
  Object.entries(data).forEach(([key, value]) => {
    if (key == 'City') { city.push(value) }
    else if (key == 'Latitude') { lat.push(value) }
    else if (key == 'Longitude') { lon.push(value)}
    else { CrimeRate.push(value) }
  })
})

// Loop through data
for (var i = 0; i < city[0].length; i++) {
  // Add a new marker to the cluster group and bind a pop-up
  console.log(typeof (lat[i]));console.log(typeof (lon[i]))
  markers.addLayer(L.marker([lat[0][i], lon[0][i]])
    .bindPopup("<h1>" + city[0][i] + "</h1> <hr> <h2>" + "Crime Rate: " + CrimeRate[0][i] + "% </h2>"));
};

// Add our marker cluster layer to the map
myMap.addLayer(markers);