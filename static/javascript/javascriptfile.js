
"use strict";


function showMap() {
    const button = document.getElementById('search_btn')
    button.addEventListener("click", initMap);
};





function initMap2(){

}


function initMap() {
    console.log('running')
    const postalCode = document.getElementById('zpsrch').value
    console.log(postalCode)

    const queryString = new URLSearchParams({"zpsrch": postalCode}).toString();
    const url = `/jsonifycoordinates?${queryString}`

    fetch(url)
        .then(response => response.json())
        .then(json_places => {
            console.log('Received response')
            console.log(json_places)
            const keys=Object.keys(json_places)
            const map = new google.maps.Map(document.getElementById("map"), {
                center: {
                    lat: json_places[keys[0]]['lat'],
                    lng: json_places[keys[0]]['long'],
                },
                scrollwheel: false,
                zoom: 13,
                zoomControl: true,
                panControl: false,
                streetViewControl: false,
                mapTypeId: google.maps.MapTypeId.TERRAIN
            });
            for (const place of keys) {
                const place_lat = json_places[place]['lat']
                const place_long = json_places[place]['long']
                const place_name = json_places[place]['name']

                const marker = new google.maps.Marker({
                    position: {
                        lat: place_lat,
                        lng: place_long,
                    },
                    title: place_name,
                   
                    map, // same as saying map: map
                });
                const placeInfo = new google.maps.InfoWindow();;

                const InfoContent = `
        

                <ul class="bear-info">
                    <li><b>Business name: </b>${place_name}</li>
                    
                </ul>
                </div>
                `;
                
                marker.addListener('click', () => {
                        placeInfo.close();
                        placeInfo.setContent(InfoContent);
                        placeInfo.open(map, marker);
                      });
               
            }
        })
};

showMap();