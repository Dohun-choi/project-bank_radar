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
        </div>

        <div v-for="(recomand, index)  in travelDestinations" :key="recomand.id">
            <p> {{ index + 1 }}번째 추천 여행지</p>
            <p> 국가명 : {{ recomand.country }}</p>
            <p> 평균 경비(원) : {{ recomand.cost }}</p>
            <p> 추천 기간(월) {{ recomand.when }}</p>
            <hr>
        </div>

    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';

const store = useCounterStore()
const selectedPeriod = ref(null)
const periods = [6, 12, 24, 36]
const travelDestinations = ref(null)


const searchTravel = () =>{

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
        selectedPeriod.value = null
    })
    .catch((err)=>{
        console.log('travel 가져오기 실패', err)
        alert(err.response.data.detail)
    })
}


</script>

<style  scoped>

</style>