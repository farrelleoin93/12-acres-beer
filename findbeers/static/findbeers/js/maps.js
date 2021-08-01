let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(-33.91722, 151.23064),
    zoom: 16,
  });
  const features = [{
      position: new google.maps.LatLng(-33.91721, 151.2263),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.91539, 151.2282),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.91747, 151.22912),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.9191, 151.22907),
      type: "info",
    },
  ];
  const offlicences = [{
      position: new google.maps.LatLng(-33.91725, 151.23011),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.91872, 151.23089),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.91784, 151.23094),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.91682, 151.23149),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.9179, 151.23463),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.91666, 151.23468),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.916988, 151.23364),
      type: "info",
    },
    {
      position: new google.maps.LatLng(-33.91662347903106, 151.22879464019775),
      type: "parking",
    },
    {
      position: new google.maps.LatLng(-33.916365282092855, 151.22937399734496),
      type: "parking",
    },
  ];

  // Create markers.
  if ($("#bars").click(function () {
      for (let i = 0; i < features.length; i++) {
        const marker = new google.maps.Marker({
          position: features[i].position,
          map: map,
        });
      }
    }));
    else if ($("#offlicences").click(function () {
      for (let i = 0; i < offlicences.length; i++) {
        const marker = new google.maps.Marker({
          position: offlicences[i].position,
          map: map,
        });
      }
    }));

}

// let offlicences = [{
//     coords: {
//         lat: 50.416308,
//         lng: -5.099469
//     }, 
// },
// ]

// // Initaiates the map
// function initMap() {
//     map = new google.maps.Map(document.getElementById("map"), {
//         zoom: 13,
//         center: new google.maps.LatLng(21.038598, 105.83044),
//     });
// }

// $(document).ready(function () {
//     $("#offlicences").click(function () {
//         initMap(offlicences);
//     // });
//     // $(".restaurants").click(function () {
//     //     clearMarkers();
//     //     displayLocationsOfType(["restaurant"]);
//     // });
//     // $(".cafes").click(function () {
//     //     clearMarkers();
//     //     displayLocationsOfType(["cafe"]);
//     // });
//     // $(".hotels").click(function () {
//     //     clearMarkers();
//     //     displayLocationsOfType(["lodging"]);
//     // });
//     // $(".attractions").click(function () {
//     //     clearMarkers();
//     //     displayLocationsOfType(["tourist_attraction"]);
//     });
// });

// // document.getElementById("offlicences").addEventListener("click", () => {
// //     initMap(offlicences);
// // });