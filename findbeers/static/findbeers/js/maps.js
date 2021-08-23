let map;

let barLocations = [{
  coords: {
      lat: 52.83700499391035,
      lng: -6.931304107938706
  }, // Tullys Bar Carlow
  content: `<h4 class="info-head">Tullys Bar Carlow</h4>
  <h6 class="info-address">148-149 Tullow St, Graigue, Carlow, R93 W243, Ireland</h6>
  <div class="info-content">Phone:<span class="phone-num">+353599131862</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://www.tullysbarcarlow.ie/"></span>http://www.tullysbarcarlow.ie/</a></div>`
},
{
  coords: {
      lat: 52.83633910026991, 
      lng: -6.929554277251607
  }, // Dinn Ri Carlow
  content: `<h4 class="info-head">Dinn Rí Carlow</h4>
  <h6 class="info-address">Tullow St, Graigue, Carlow</h6>
  <div class="info-content">Phone:<span class="phone-num">+353599133111</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://www.dinnri.com/"></span>http://www.dinnri.com/</a></div>`
},
{
  coords: {
      lat: 52.84335168035547,
      lng: -6.9773936
  }, // The Mall Laois
  content: `<h4 class="info-head">The Mall</h4>
  <h6 class="info-address">Clonmore, Killeshin, Co. Laois</h6>
  <div class="info-content">Phone:<span class="phone-num">+353599143407</span></div>`
},
{
  coords: {
      lat: 52.60054254598292, 
      lng: -6.924515725214058
  }, // O'Shea's Pub Borris
  content: `<h4 class="info-head">O'Shea's Pub</h4>
  <h6 class="info-address">Main St, Knocknagundarragh, Carlow, R95 C92R</h6>
  <div class="info-content">Phone:<span class="phone-num">+353599773106</span></div>`
},
{
  coords: {
      lat: 52.83914939690085, 
      lng: -6.930131769312902
  }, // Carpe Diem Carlow
  content: `<h4 class="info-head">Carpe Diem Carlow</h4>
  <h6 class="info-address">Court Pl, Graigue, Carlow</h6>
  <div class="info-content">Phone:<span class="phone-num">+353599134580</span></div>`
},
{
  coords: {
      lat: 52.65525446015407, 
      lng: -7.247006199999999
  }, // Billy Byrnes Gastro Bar & Venue
  content: `<h4 class="info-head">Billy Byrnes Gastro Bar & Venue</h4>
  <h6 class="info-address">Court Pl, Graigue, Carlow</h6>
  <div class="info-content">Phone:<span class="phone-num">+353056 772 1783</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.billybyrnes.com/"></span>https://www.billybyrnes.com/</a></div>`
},
{
  coords: {
      lat: 52.65552349097606, 
      lng: -7.255362361374195
  }, // Cleere's Bar & Theatre
  content: `<h4 class="info-head">Cleere's Bar & Theatre</h4>
  <h6 class="info-address">28 Parliament St, Gardens, Kilkenny, R95 YR61</h6>
  <div class="info-content">Phone:<span class="phone-num">+353567762573</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.billybyrnes.com/"></span>https://www.billybyrnes.com/</a></div>`
},
{
  coords: {
      lat: 52.65357911687143, 
      lng: -7.248154192595156
  }, // Bridie's Bar & General Store
  content: `<h4 class="info-head">Bridie's Bar & General Store</h4>
  <h6 class="info-address">72 John Street Lower, Collegepark, Kilkenny, R95 X890</h6>
  <div class="info-content">Phone:<span class="phone-num">+353567765133</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://www.langtons.ie/"></span>http://www.langtons.ie/</a></div>`
},
{
  coords: {
      lat: 52.650990068254934, 
      lng: -7.251544738625804
  }, // Left Bank
  content: `<h4 class="info-head">Left Bank</h4>
  <h6 class="info-address">1 The Parade, Gardens, Kilkenny</h6>
  <div class="info-content">Phone:<span class="phone-num">+353567750016</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://www.leftbank.ie/"></span>http://www.leftbank.ie/</a></div>`
},
{
  coords: {
      lat: 52.526726018498735, 
      lng: -7.135754915877413
  }, // Tim's Bar
  content: `<h4 class="info-head">Tim's Bar</h4>
  <h6 class="info-address">The Quay, Thomastown, Co. Kilkenny</h6>
  <div class="info-content">Phone:<span class="phone-num">+353877453209</span></div>`
},
{
  coords: {
      lat: 53.034006338121095,
      lng: -7.302118961374197
  }, // Square Bar
  content: `<h4 class="info-head">Square Bar</h4>
  <h6 class="info-address">8 Market Square, Kylekiproe, Portlaoise, Co. Laois, R32 YX0T</h6>
  <div class="info-content">Phone:<span class="phone-num">+35356456832</span></div>`
},
{
  coords: {
      lat: 52.650990068254934, 
      lng: -7.251544738625804
  }, // E.J.Morrissey
  content: `<h4 class="info-head">E.J.Morrissey</h4>
  <h6 class="info-address">Kylekiproe, Portlaoise, Co. Laois</h6>
  <div class="info-content">Phone:<span class="phone-num">+353578678905</span></div>`
},
{
  coords: {
      lat: 53.13314929382657, 
      lng: -7.150533738625803
  }, // The Heritage Golf Resort
  content: `<h4 class="info-head">The Heritage Golf Resort</h4>
  <h6 class="info-address">Killenard, Co. Laois</h6>
  <div class="info-content">Phone:<span class="phone-num">+353578642321</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://www.heritageresort.ie/"></span>http://www.heritageresort.ie/</a></div>`
},
{
  coords: {
      lat: 53.044476412794424, 
      lng: -7.266581861374196
  }, // O'Gormans Bar & Restaurant
  content: `<h4 class="info-head">O'Gormans Bar & Restaurant</h4>
  <h6 class="info-address">Kilminchy Court, Kilminchy, Portlaoise, Co. Laois, R32 DTW5</h6>
  <div class="info-content">Phone:<span class="phone-num">+353567750016</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://www.leftbank.ie/"></span>http://www.leftbank.ie/</a></div>`
},
{
  coords: {
      lat: 52.991944816222095, 
      lng: -6.987165553969354
  }, // The Duke
  content: `<h4 class="info-head">The Duke</h4>
  <h6 class="info-address">Duke St, Athy, Co. Kildare, R14 VK06</h6>
  <div class="info-content">Phone:<span class="phone-num">+353598638947</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://theduke.ie/"></span>http://theduke.ie/</a></div>`
},
{
  coords: {
      lat: 52.650990068254934, 
      lng: -7.251544738625804
  }, // McCormacks Pub
  content: `<h4 class="info-head">McCormacks Pub</h4>
  <h6 class="info-address">37 S Main St, Naas East, Naas, Co. Kildare, W91 R772</h6>
  <div class="info-content">Phone:<span class="phone-num">+35345897686</span></div>`
},
{
  coords: {
      lat: 52.39896050722988, 
      lng: -6.937355915343549
  }, // Whelans
  content: `<h4 class="info-head">Whelans</h4>
  <h6 class="info-address">14 Irishtown, New Ross, Co. Wexford</h6>
  <div class="info-content">Phone:<span class="phone-num">+353578682467</span></div>`
},
{
  coords: {
      lat: 52.650990068254934, 
      lng: -7.251544738625804
  }, // Simon Lambert & Sons
  content: `<h4 class="info-head">Simon Lambert & Sons</h4>
  <h6 class="info-address">37 S Main St, Slippery Green, Wexford, Y35 H725</h6>
  <div class="info-content">Phone:<span class="phone-num">+353539180041</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://www.simonlambertandsons.ie/menu"></span>http://www.simonlambertandsons.ie/menu</a></div>`
},
{
  coords: {
      lat: 52.26271752275906, 
      lng: -7.114475507938705
  }, // Tully's Bar Waterford
  content: `<h4 class="info-head">Tully's Bar Waterford</h4>
  <h6 class="info-address">37 O'Connell St, Waterford, X91 AY62</h6>
  <div class="info-content">Phone:<span class="phone-num">+35351301639</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="http://www.tullysbar.ie/"></span>http://www.tullysbar.ie/</a></div>`
},
{
  coords: {
      lat: 52.26279148941446,
      lng: -7.11792696877904
  }, // Henry Downes
  content: `<h4 class="info-head">Henry Downes</h4>
  <h6 class="info-address">10 Thomas St, Waterford</h6>
  <div class="info-content">Phone:<span class="phone-num">+35351874118</span></div>`
},
{
  coords: {
      lat: 52.26405807590981, 
      lng:  -7.1179451
  }, // An Uisce Beatha
  content: `<h4 class="info-head">An Uisce Beatha</h4>
  <h6 class="info-address">8 Merchants Quay, Waterford, X91 PR27</h6>
  <div class="info-content">Phone:<span class="phone-num">+353834799649</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.facebook.com/An-Uisce-Beatha-883077578445830/"></span>https://www.facebook.com/An-Uisce-Beatha-883077578445830/</a></div>`
},
];



let shopLocations = [{
  coords: { 
      lat: 52.83616160443315,
      lng: -6.928720492595158
  }, // O'Briens Wine Off-Licence Carlow
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Carlow</h4>
  <h6 class="info-address">Exchequer House, Potato Market, Graigue, Carlow, R93 F3X8, Ireland</h6>
  <div class="info-content">Phone:<span class="phone-num">+353599139814</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 53.31653536209059,
      lng: -6.265507230687798
  }, // O'Briens Wine Off-Licence Rathmines
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Rathmines</h4>
  <h6 class="info-address">149 Rathmines Rd Upper, Rathmines, Dublin, D06 F793</h6>
  <div class="info-content">Phone:<span class="phone-num">(01) 496 7811</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 53.17869080472516,
      lng: -6.800015430687098
  }, // O'Briens Wine Off-Licence Newbidge
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Newbridge</h4>
  <h6 class="info-address">1 Courtyard Shopping Centre, Newbridge, Co. Kildare</h6>
  <div class="info-content">Phone:<span class="phone-num">+35345449804</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 53.24029093263878,
      lng: -6.660667907938706
  }, // O'Briens Wine Off-Licence Naas
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Naas</h4>
  <h6 class="info-address">Unit 20 Monread Shopping Centre, Naas, Co. Kildare</h6>
  <div class="info-content">Phone:<span class="phone-num">+35345901038</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 53.29875957050485, 
      lng: -6.303425646030648
  }, // O'Briens Wine Off-Licence Templeogue
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Templeogue</h4>
  <h6 class="info-address">Unit 1, 178 Templeogue Rd, Templeogue Village, Dublin, D6W PT88</h6>
  <div class="info-content">Phone:<span class="phone-num">+35314920334</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 53.28925211082863,
      lng: -6.204697538625804 
  }, // O'Briens Wine Off-Licence Stillorgan
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Stillorgan</h4>
  <h6 class="info-address">2 Lower Kilmacud Rd, Stillorgan, Dublin, A94 F898</h6>
  <div class="info-content">Phone:<span class="phone-num">+35312836287</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 53.71419196068865, 
      lng: -6.352210899999999
  }, // O'Briens Wine Off-Licence Drogheda
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Drogheda</h4>
  <h6 class="info-address">The Haymarket, Unit 5, Drogheda, Co. Louth, A92 XC82</h6>
  <div class="info-content">Phone:<span class="phone-num">+35314920334</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 53.312815554631264, 
      lng: -6.274150238625804
  }, // O'Briens Wine Off-Licence Rathgar
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Rathgar</h4>
  <h6 class="info-address">105 Rathgar Rd, Rathfarnham, Dublin 6, D06 E2T3</h6>
  <div class="info-content">Phone:<span class="phone-num">+35314909366</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 52.6637950990123,
      lng: -8.596110723282255
  }, // O'Briens Wine Off-Licence Limerick
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Limerick</h4>
  <h6 class="info-address">Parkway Shopping Centre, Unit 8, Castletroy, Co. Limerick, V94 PP94</h6>
  <div class="info-content">Phone:<span class="phone-num">+35361422559</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 51.878742680438116,
      lng: -8.432209353969355 
  }, // O'Briens Wine Off-Licence Cork
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Cork</h4>
  <h6 class="info-address">Unit 13, 14 Douglas Relief Rd, Douglas, Cork, T12 E659</h6>
  <div class="info-content">Phone:<span class="phone-num">+353214369596</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
{
  coords: { 
      lat: 52.247656475594574,
      lng: -7.0833117 
  }, // O'Briens Wine Off-Licence Waterford
  content: `<h4 class="info-head">O'Briens Wine Off-Licence Waterford</h4>
  <h6 class="info-address">Unit 42 Ardkeen Shopping Centre, Dunmore Rd, Ardkeen, Waterford</h6>
  <div class="info-content">Phone:<span class="phone-num">+35351560457</span></div>
  <div class="info-content">Website:<span class="info-website"><a target="blank" href="https://www.obrienswine.ie/"></span>https://www.obrienswine.ie/</a></div>`
},
];


function initMap(selectedLocations) {
  map = new google.maps.Map(document.getElementById("map"), {
      zoom: 7,
      center: new google.maps.LatLng(53.24986489838344, -7.759362072216498),
  });

  let labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Iterate through the array of locations and place the markers on the map

    if (selectedLocations) {
        for (let i = 0; i < selectedLocations.length; i++) {
            let marker = new google.maps.Marker({
                position: selectedLocations[i].coords,
                map: map,
                animation: google.maps.Animation.DROP,
            });

            // Create info window

            const infowindow = new google.maps.InfoWindow({
                content: selectedLocations[i].content,
            });

            // Close previous info window when new info window opened

            google.maps.event.addListener(marker, 'click', function () {
                if (currentInfoWindow != null) {
                    currentInfoWindow.close();
                }

                infowindow.open(map, marker);
                currentInfoWindow = infowindow;
            });

            var currentInfoWindow = null;
        }
    }
}

$(document).ready(function () {
  $("#bars").click(function () {
    initMap(barLocations);
  });
});

$(document).ready(function () {
  $("#offlicences").click(function () {
    initMap(shopLocations);
  });
});
