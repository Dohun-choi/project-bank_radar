<template>
    <div>
        <div>
            <form @submit.prevent="searchTeravel">
                <select v-model="selectedCountry">
                    <option v-for=" country in countrys" :value="country" :key="country">
                        {{ country }}
                    </option>
                </select>
            <input type="submit" value="여행지에 따른 적금상품 추천">
            </form>
        </div>


        <div v-for="(recomand, index)  in recomandItem" :key="recomand.id">
            <div @click="goSavingsDetail(recomand.fin_prdt_cd)">
                <p>{{ index + 1 }}번째 추천 적금상품 (눌러서 상세보기)</p>
                <p> {{ recomand.kor_co_nm }} - {{ recomand.fin_prdt_nm }}</p>
                <p> 기준 금리 : {{ recomand.intr_rate }}</p>
                <p> 최고 금리 : {{ recomand.intr_rate2 }}</p>
                <hr>
            </div>
        </div>


    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';
import { useRouter } from 'vue-router';


const router = useRouter()
const store = useCounterStore()
const selectedCountry = ref(null)
const countrys = ['Korea', 'USA', 'JAPAN']
const recomandItem = ref(null)


const searchTeravel = () => {
    axios({
        method: 'GET',
        url: `${store.API_URL}/api/v1/recommend/travel/${selectedCountry.value}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log('travel 가져오기 성공', res.data);
        recomandItem.value = res.data
        selectedCountry.value = null
    })
    .catch((err)=>{
        console.log('travel 가져오기 실패', err)
        alert(err.response)
    })
}

const goSavingsDetail = (key) => {
    router.push({
        name: 'SavingsDetail',
        params:{key: key},
    })
}

</script>

<style  scoped>

</style>