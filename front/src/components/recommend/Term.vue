<template>
<div class="container mt-5">
    <h3 class="title mb-3">저축기간에 따라 여행지 추천받기</h3>

    <form @submit.prevent="searchTravel" class="mb-3 d-flex">
    <select v-model="selectedPeriod" class="form-select mr-2">
        <option v-for="period in periods" :value="period" :key="period">
        {{ period }}개월
        </option>
    </select>
    <input type="number" placeholder="월 적금액" v-model="monthly">
    <input type="submit" value="검색하기" class="btn btn-primary">
    </form>

    <div class="row">
    <div v-for="(recommend, index) in travelDestinations" :key="recommend.id" class="col-md-4 mb-3">
        <a class="no-decoration" :href="`https://www.google.co.kr/search?q=${recommend.country}`" target="_blank">
        <div class="card" @click="goSavingsDetail(recommend.fin_prdt_cd)">
        <img :src="recommend.img_url" class="card-img-top" alt="Product Image">
        <div class="card-body">
            <h5 class="card-title">{{ index + 1 }}번째 추천 여행지</h5>
            <p class="card-text">국가명: {{ recommend.country }}</p>
            <p class="card-text">평균 경비(원): {{ recommend.cost }}</p>
            <p class="card-text">추천 기간(월): {{ recommend.when.replace(/,/g,' ') }}</p>
        </div>
        </div>
        </a>
    </div>
    </div>
</div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';
import { useRouter } from 'vue-router';
import 'bootstrap/dist/css/bootstrap.min.css';

const router = useRouter();
const store = useCounterStore();
const selectedPeriod = ref(null);
const periods = [6, 12, 24, 36];
const travelDestinations = ref(null);
const monthly = ref(null)

const searchTravel = () => {
    const config = {
        method: 'GET',
        url: `${store.API_URL}/api/v1/recommend/travel/${selectedPeriod.value}`,
        headers: {
        Authorization: `Token ${store.token}`
        },
        params : {
            monthly_saving: null,
            intr_rate_type: 'S',
            period: 6
        }
    }

    if (monthly.value && typeof monthly.value !== 'number') {
        return alert('숫자를 입력해 주세요')
    } else if (monthly.value && monthly.value < 99) {
        return alert('너무 작은 숫자입니다.')
    }

    if (typeof monthly.value === 'number' && monthly.value >= 100) {
        config.params.monthly_saving = monthly.value
    }



    axios(config)
    .then((res) => {
    console.log('travel 가져오기 성공', res.data);
    travelDestinations.value = res.data;
    selectedPeriod.value = null;
    })
    .catch((err) => {
    console.log('travel 가져오기 실패', err);
    alert(err.response.data.detail);
    });
};

const goSavingsDetail = (key) => {
router.push({
    name: 'SavingsDetail',
    params: { key: key },
});
};
</script>

<style scoped>
.title {
color: #00376b; /* 네이버 블루 */
border-bottom: 2px solid #00376b;
padding-bottom: 0.5rem;
}

.container {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
}
.card {
cursor: pointer;
transition: transform 0.3s ease-in-out;
}

.card:hover {
transform: scale(1.05);
}

.card-img-top {
border-top-left-radius: 10px;
border-top-right-radius: 10px;
object-fit: cover;
height: 200px;
}

.card-body {
padding: 1.25rem;
}

.card-title {
font-size: 1.5rem;
margin-bottom: 0.75rem;
}

.card-text {
margin-bottom: 0.5rem;
}
.btn-primary {
    background-color: #00376b;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.row {
margin-top: 1rem;
}

.no-decoration {
    text-decoration: none; /* Removes underline */
    color: inherit; /* Inherits color from its parent */
}
</style>
