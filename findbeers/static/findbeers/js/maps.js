let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(53.24986489838344, -7.759362072216498),
    zoom: 7,
  });
  const 

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