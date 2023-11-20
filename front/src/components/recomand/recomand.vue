<template>
    <div>
        <h2>상품 추천 받기</h2>
        <div>
            <form @submit.prevent="searchTravel">
                <select v-model="selectedPeriod">
                    <option v-for=" period in periods" :value="period" :key="period">
                        {{ period }}개월
                    </option>
                </select>
            <input type="submit" value="저축 기간에 따른 여행지 추천">
            </form>

            <!-- teravel 오타 수정해야 함 -->
            <form @submit.prevent="searchTeravel">
                <select v-model="selectedCountry">
                    <option v-for=" country in countrys" :value="country" :key="country">
                        {{ country }}
                    </option>
                </select>
            <input type="submit" value="여행지에 따른 적금상품 추천">
            </form>
        </div>

        <div v-if="isViewTravel" v-for="(recomand, index)  in travelDestinations" :key="recomand.id">
            <p> {{ index + 1 }}번째 추천 여행지</p>
            <p> 국가명 : {{ recomand.country }}</p>
            <p> 평균 경비(원) : {{ recomand.cost }}</p>
            <p> 추천 기간(월) {{ recomand.when }}</p>
            <hr>
        </div>

        <div v-if="isViewTeravel">
            
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';


const store = useCounterStore()

const isViewTravel = ref(true)
const isViewTeravel = ref(false)

const selectedPeriod = ref(null)
const selectedCountry = ref(null)

const periods = [6, 12, 24, 36]
const countrys = ['Korea', 'UAE', 'Australia']

const travelDestinations = ref(null)
const recomandItem = ref(null)

const searchTravel = () =>{
    isViewTravel.value = true
    isViewTeravel.value = false
    console.log(selectedPeriod.value)
    // 저축 기간에 따른 여행지 추천 데이터 가져오기
    axios({
        method: 'GET',
        url: `${store.API_URL}/api/v1/recommend/travel/${selectedPeriod.value}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log('travel 가져오기 성공', res.data);
        travelDestinations.value = res.data
    })
    .catch((err)=>{
    console.log('travel 가져오기 실패', err)
    alert(err.response.data.detail)
    })
}

const searchTeravel = () => {
    isViewTravel.value = false
    isViewTeravel.value = true
    console.log(selectedCountry.value)
    // 여행지에 따른 적금 상품 추천
    axios({
        method: 'GET',
        url: `${store.API_URL}/api/v1/recommend/teravel/${selectedCountry.value}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log('travel 가져오기 성공', res);
        recomandItem.value = res

    })
    .catch((err)=>{
    console.log('travel 가져오기 실패', err)
    alert(err.response)
    })
}


</script>

<style  scoped>

</style>