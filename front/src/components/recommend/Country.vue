<template>
<div class="container mt-5">
    <h3 class="title mb-3">여행지에 따른 적금상품 추천 받기 </h3>
    <form @submit.prevent="searchTravel" class="mb-3">
    <div class="d-flex">
        <select v-model="selectedCountry" class="form-select mr-2">
        <option v-for="country in countrys" :value="country" :key="country">
            {{ country }}
        </option>
        </select>
        <input type="submit" value="검색하기" class="btn btn-primary">
    </div>
    </form>

    <div>
    <div v-for="(recommend, index) in recommendItem" :key="recommend.id" class="mb-3">
        <div @click="goSavingsDetail(recommend.fin_prdt_cd)" class="card recommend-card">
        <img src="https://www.infostockdaily.co.kr/news/photo/202309/194484_182936_411.jpg" class="card-img-top" alt="Product Image">
        <div class="card-body">
            <h5 class="card-title">{{ index + 1 }}번째 추천 적금상품</h5>
            <p class="card-text">{{ recommend.kor_co_nm }} - {{ recommend.fin_prdt_nm }}</p>
            <div class="row">
            <div class="col-md-6">
                <p class="card-text">기준 금리: {{ recommend.intr_rate }}</p>
            </div>
            <div class="col-md-6">
                <p class="card-text">최고 금리: {{ recommend.intr_rate2 }}</p>
            </div>
            </div>
        </div>
        <hr class="m-0">
        </div>
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
const selectedCountry = ref(null);
const countrys = ['Korea', 'USA', 'Australia', 'Bahrain', 'Brunei-Darussalam', 'Canada', 'Swiss', 'China', 'Denmark', 'EU', 'UK', 'HongKong', 'Indonesia', 'Japan', 'Kuwait', 'Malaysia', 'Norway', 'New-Zealand', 'Saudi-Arabia', 'Sweden', 'Singapore', 'Thailand', 'UAE'];
const recommendItem = ref(null);

const searchTravel = () => {
axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/recommend/travel/${selectedCountry.value}`,
    headers: {
    Authorization: `Token ${store.token}`,
    },
})
    .then((res) => {
    console.log('travel 가져오기 성공', res.data);
    recommendItem.value = res.data;
    selectedCountry.value = null;
    })
    .catch((err) => {
    console.log('travel 가져오기 실패', err);
    alert(err.response);
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
.container {
background-color: #ffffff;
border-radius: 10px;
box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
padding: 20px;
}

.btn-primary {
background-color: #00376b;
color: #ffffff;
border: none;
border-radius: 5px;
cursor: pointer;
}

.btn-primary:hover {
background-color: #001f3f;
}

.recommend-card {
cursor: pointer;
transition: transform 0.3s ease-in-out;
}

.recommend-card:hover {
transform: scale(1.05);
}

.card-img-top {
border-top-left-radius: 10px;
border-top-right-radius: 10px;
object-fit: cover;
max-width: 100%;
height: auto;
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

.row {
margin-top: 1rem;
}

.col-md-6 {
padding: 0 1rem;
}

hr {
border-top: 1px solid #dee2e6;
margin: 0;
}

.title {
color: #00376b; /* 네이버 블루 */
border-bottom: 2px solid #00376b;
padding-bottom: 0.5rem;
}

.btn {
margin: 5px;
}
</style>
