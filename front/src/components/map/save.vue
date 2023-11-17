<template>
    <div>
        <form @submit.prevent="searchPlaces">
            <input type="text" v-model="search">
            <input type="submit" value="검색하기">
        </form>
        <div id="map"></div>
    </div>
    </template>
    
    <script setup>
    import { ref, onMounted } from 'vue';
    
    const search = ref(null);
    const map = ref(null);
    const infowindow = ref(null);
    const ps = ref(null);
    
    // 지도 그리기
    const initMap = () => {
        const container = document.getElementById('map');
        const options = {
            center: new kakao.maps.LatLng(37.566826, 126.9786567),
            level: 5,
        };
    
        // 지도 객체 소환
        map.value = new kakao.maps.Map(container, options);
    
        infowindow.value = new kakao.maps.InfoWindow({ zIndex: 1 });
    
        ps.value = new kakao.maps.services.Places(map);
        
        ps.value.categorySearch('BK9', placesSearchCB, {useMapBounds:true});
    
    };
    
    // // 키워드 검색 완료 시 호출되는 콜백함수(키워드)
    // const placesSearchCB = (data, status, pagination) => {
    // if (status === kakao.maps.services.Status.OK) {
    //     const bounds = new kakao.maps.LatLngBounds();
    
    //     for (let i = 0; i < data.length; i++) {
    //     displayMarker(data[i]);
    //     bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    //     }
    
    //     map.value.setBounds(bounds);
    // }
    // };
    
    
    // 카테고리 검색 완료 시 호출되는 콜백함수 입니다
    function placesSearchCB (data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {
            for (let i=0; i<data.length; i++) {
                displayMarker(data[i]);    
            }       
        }
    }
    
    // 지도에 마커를 표시하는 함수
    const displayMarker = (place) => {
        const marker = new kakao.maps.Marker({
            map: map.value,
            position: new kakao.maps.LatLng(place.y, place.x),
        });
    
        // 마커 이벤트 - 마커 클릭시 장소명이 인포윈도우에 표출
        kakao.maps.event.addListener(marker, 'click', function () {
            infowindow.value.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
            infowindow.value.open(map.value, marker);
        });
    };
    
    // // input에 입력 시 검색 실행
    // const searchPlaces = () => {
    // ps.value.keywordSearch(search.value, placesSearchCB);
    // console.log('keyword',ps.value)
    // ps.value.categorySearch('BK9', placesSearchCB, { useMapBounds: true});
    // console.log('catagory', ps.value)
    
    // };
    
    
    // 지도 소환
    onMounted(async() => {
    if (window.kakao && window.kakao.maps) {
        initMap();
    } else {
        const script = document.createElement('script');
        script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=2d0dddc1e7df6701773748a3e6aad825&libraries=services`;
        document.head.appendChild(script);
        script.onload = () => {
        kakao.maps.load(initMap);
        };
    }
    });
    </script>
    
    <style scoped>
    #map {
    width: 400px;
    height: 400px;
    }
    </style>
    