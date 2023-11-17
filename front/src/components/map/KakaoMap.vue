<template>
    <div>
        <p>시 / 구 / 은행 입력하세요</p>
        <form @submit.prevent="searchPlaces">
            <!-- 시 -->
            <select v-model="first">
                <option v-for="s in si" :value="s" :key="s">
                    {{ s }}
                </option>
            </select>
            <!-- 구 -->
            <select v-model="second">
                <option v-for="g in gu" :value="g" :key="g">
                    {{ g }}
                </option>
            </select>
            <!-- 은행 -->
            <select v-model="third">
                <option v-for="b in bank" :value="b" :key="b">
                    {{ b }}
                </option>
            </select>
            <input type="submit" value="검색하기">
        </form>
        <p>{{ first }} {{ second }} {{ third }}</p>
        <div id="map"></div>
    </div>
    </template>
    
    <script setup>
    import { ref, onMounted } from 'vue';
    
    const first = ref('')
    const second = ref('')
    const third = ref('')

    const si = ['서울', '부산', '대구', '울산']
    const gu = ['진구', '사하구', '강서구']
    const bank = ['국민은행', '신한은행']

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
        
    
    };
    
    // 키워드 검색 완료 시 호출되는 콜백함수(키워드)
    const placesSearchCB = (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
        const bounds = new kakao.maps.LatLngBounds();
    
        for (let i = 0; i < data.length; i++) {
        displayMarker(data[i]);
        bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
        }
    
        map.value.setBounds(bounds);
    }
    };
    
    

    
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
    
    // input에 입력 시 검색 실행
    const searchPlaces = () => {
    ps.value.keywordSearch(`${first.value} ${second.value} ${third.value}`, placesSearchCB);

    };
    
    
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
    