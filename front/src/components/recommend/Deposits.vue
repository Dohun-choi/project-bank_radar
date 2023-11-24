<template>
<div class="container mt-5">
    <h2 class="title mb-3">키워드에 따른 예금 상품 추천</h2>

    <form @submit.prevent="searchDeposits" class="mb-3">
    <div class="d-flex">
        <select v-model="selectedOption" class="form-select mr-2">
        <option v-for="v, k in options" :value="v" :key="k">
            {{ k }}
        </option>
        </select>
        <input type="submit" value="추천 받기" class="btn btn-primary">
    </div>
    </form>

    <div>
    <div v-for="(recommend, index) in recomandDeposit" :key="recommend.id" class="card mb-3" @click="goDetail(recommend.fin_prdt_cd)">
        <div class="card-body">
        <h5 class="card-title">{{ index + 1 }}번째 추천 상품 (눌러서 상세보기)</h5>
        <p class="card-text">{{ recommend.kor_co_nm }} - {{ recommend.fin_prdt_nm }}</p>
        <p class="card-text">금리: {{ recommend.intr_rate }}%</p>
        <p class="card-text">예금기간: {{ recommend.save_trm }}개월</p>
        </div>
        <hr class="m-0">
    </div>
    </div>
</div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useCounterStore();
const recomandDeposit = ref(null);
const selectedOption = ref(null);
const options = {'나이': 'age', '월 수입' : 'monthly_income', '자산' :'assets', '가입자 수':'likes'}

const searchDeposits = () => {
axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/recommend/deposits/${selectedOption.value}`,
    headers: {
    Authorization: `Token ${store.token}`,
    },
})
    .then((res) => {
    console.log('추천 정보 가져오기 성공', res.data);
    recomandDeposit.value = res.data;
    selectedOption.value = null;
    })
    .catch((err) => {
    console.log('추천 정보 가져오기 실패', err);
    alert(err.response.data.detail);
    });
};

const goDetail = (key) => {
router.push({
    name: 'DepositsDetail',
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

.card {
cursor: pointer;
transition: transform 0.3s ease-in-out;
}

.card:hover {
transform: scale(1.05);
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

hr {
border-top: 1px solid #dee2e6;
margin: 0;
}

.title {
color: #00376b; /* 네이버 블루 */
border-bottom: 2px solid #00376b;
padding-bottom: 0.5rem;
}
</style>
