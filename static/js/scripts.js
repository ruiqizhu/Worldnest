$(document).ready(function() {
    $('select').material_select();
    $('.carousel').carousel();
    // Next slide
    $('.carousel').carousel('next');
    $('.carousel').carousel('next', [3]); // Move next n times.
    // Previous slide
    $('.carousel').carousel('prev');
    $('.carousel').carousel('prev', [4]); // Move prev n times.

    // Pause slider
    $('.slider').slider('pause');
    // Start slider
    $('.slider').slider('start');
    // Next slide
    $('.slider').slider('next');
    // Previous slide
    $('.slider').slider('prev');
    $('.slider').slider({full_width: true});

    $('.parallax').parallax();
    });


function initMap() {
  var myLatLng = {lat: -25.363, lng: 131.044};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}

(function(window, google){
  // map options
  var options = {
    center: {
      lat:37.791350,
      lng:-122.435883
    },
    zoom: 10
  },
  element = document.getElementById('map-canvas')
  // map
  map = new google.maps.Map(element, options);
  
}(window, google));
