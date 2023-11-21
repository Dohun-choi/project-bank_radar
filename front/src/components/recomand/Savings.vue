<template>
    <div>
        <h2>상품 추천 받기</h2>

        <div>
            <form @submit.prevent="searchSavings">
                <select v-model="selectedOption">
                    <option v-for=" option in options" :value="option" :key="option.id">
                        {{ option }}
                    </option>
                </select>
                <input type="submit" value="키워드에 따른 적금 상품 추천">
            </form>
        </div>

        <div v-for="(recomand, index)  in recomandSavings" :key="recomand.id" @click="goDetail(recomand.fin_prdt_cd)">
            <p> {{ index + 1 }}번째 추천 상품 ( 눌러서 상세보기)</p>
            <p>{{ recomand.kor_co_nm }} - {{ recomand.fin_prdt_nm }}</p>
            <p> 금리 : {{ recomand.intr_rate }} %</p>
            <p> 예금기간 {{ recomand.save_trm }}개월</p>
            <hr>
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
const recomandSavings = ref(null)
const selectedOption = ref (null)
const options = ['age', 'monthly_income', 'assets', 'likes']

const searchSavings = () =>{

    // 선택 사항에 따른 예금 추천
    axios({
        method: 'GET',
        url: `${store.API_URL}/api/v1/recommend/savings/${selectedOption.value}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log('추천 정보 가져오기 성공', res.data);
        recomandSavings.value = res.data
        selectedOption.value = null
    })
    .catch((err)=>{
        console.log('추천 정보 가져오기 실패', err)
        alert(err.response.data.detail)
    })
}


const goDetail = (key) => {
    router.push({
        name: 'SavingsDetail',
        params:{key: key},
}
)}

</script>

<style  scoped>

</style>