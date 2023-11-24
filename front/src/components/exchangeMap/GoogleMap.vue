<template>
    <div class="mt-4">
        <form @submit.prevent="searchPlace" class="mb-3">
        <div class="input-group">
            <input type="text" v-model="inputPlace" class="form-control" placeholder="장소 검색" />
            <button type="submit" class="btn btn-primary">검색</button>
        </div>
        </form>
        <div v-if="loading" class="alert alert-info">로딩 중...</div>
        <div id="map" style="width: 100%; height: 400px;"></div>
    </div>
    </template>
    
    <script setup>
    import { ref, onMounted } from 'vue';
    import 'bootstrap/dist/css/bootstrap.min.css';
    
    let map;
    let service;
    let infowindow;
    const inputPlace = ref('');
    const loading = ref(false);
    const selectedPlace = ref(null);
    
    const initMap = () => {
    const ssafy = new google.maps.LatLng(35.0953265, 128.8556681);
    
    infowindow = new google.maps.InfoWindow();
    map = new google.maps.Map(document.getElementById('map'), {
        center: ssafy,
        zoom: 15,
    });
    };
    
    const createMarker = (place) => {
    if (!place.geometry || !place.geometry.location) return;
    
    const marker = new google.maps.Marker({
        map,
        position: place.geometry.location,
    });
    
    google.maps.event.addListener(marker, 'click', () => {
        const request = {
        placeId: place.place_id,
        fields: ['name', 'formatted_address', 'place_id', 'geometry'],
        };
    
        service.getDetails(request, (detailedPlace, status) => {
        if (status === google.maps.places.PlacesServiceStatus.OK && detailedPlace) {
            infowindow.setContent(`<h2>${detailedPlace.name}</h2>
            <p>${detailedPlace.place_id}</p>
            <p>${detailedPlace.formatted_address}</p>`);
            infowindow.open(map, marker);
            selectedPlace.value = detailedPlace;
        }
        });
    });
    };
    
    const searchPlace = async () => {
    if (!map || !inputPlace.value || loading.value) return;
    
    loading.value = true;
    
    const request = {
        query: inputPlace.value,
        fields: ['name', 'geometry', 'place_id'],
    };
    
    service = new google.maps.places.PlacesService(map);
    service.findPlaceFromQuery(request, (results, status) => {
        loading.value = false;
    
        if (status === google.maps.places.PlacesServiceStatus.OK && results) {
        for (let i = 0; i < results.length; i++) {
            createMarker(results[i]);
        }
    
        map.setCenter(results[0].geometry.location);
        }
    });
    };
    
    onMounted(() => {
    // Load Google Maps script dynamically
    const script = document.createElement('script');
    script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyCtBwnK5R1X7BdQgcZ-nmNJnOtPbtO00lE&libraries=places&callback=initMap`;
    script.defer = true;
    script.async = true;
    script.onload = initMap; // 이 부분 추가
    document.head.appendChild(script);
    });
    </script>