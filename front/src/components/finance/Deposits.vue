<template>
<div>
    <div class="search-form">
    <p class="search-title">검색하기</p>
    <form @submit.prevent="searchProducts(selectedBank, selectedPeriod)" class="d-flex">
        <!-- 은행 -->
        <div class="form-group">
            <select v-model="selectedBank" class="form-control form-select mr-2">
                <option v-for="bank in banks" :value="bank" :key="bank">
                {{ bank }}
                </option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary ml-2">확인</button>
    </form>
</div>

    <div id="app" class="container mt-5">
    <div class="row">
        <div v-for="(item, index) in visibleItems" :key="index" class="col-md-4">
        <div class="card finance-card">
            <img @click="goDetail(item.fin_prdt_cd)" src="@/assets/eve.jpg" class="card-img-top" alt="Finance Image">
            <div class="card-body">
            <h5 class="card-title">{{ item.kor_co_nm }} - {{ item.fin_prdt_nm }}</h5>
            <table class="table table-striped finance-table">
                <tbody>
                <tr>
                    <th scope="row">공시 제출 월</th>
                    <td>{{ item.dcls_month }}</td>
                </tr>
                <tr>
                    <th scope="row">가입 제한</th>
                    <td>{{ item.dcls_month }}</td>
                </tr>
                <tr>
                    <th scope="row">가입 대상</th>
                    <td>{{ item.join_member }}</td>
                </tr>
                <tr>
                    <th scope="row">가입 방법</th>
                    <td>{{ item.join_way }}</td>
                </tr>
                <tr>
                    <th scope="row">최고한도</th>
                    <td>{{ item.max_limit }}</td>
                </tr>
                <tr>
                    <th scope="row">좋아요</th>
                    <td>{{ item.like_users }}</td>
                </tr>
                </tbody>
            </table>
            </div>
        </div>
        </div>
    </div>
    <div class="row mt-3">
        <div class="col-md-12 d-flex justify-content-center">
        <button @click="prevSlide" class="btn btn-primary mr-2" :disabled="currentIndex === 0">이전</button>
        <button @click="nextSlide" class="btn btn-primary" :disabled="currentIndex === Math.ceil(products.length / 3) - 1">다음</button>
        </div>
    </div>
    </div>
</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import 'bootstrap/dist/css/bootstrap.min.css';

const router = useRouter();
const store = useCounterStore();

const products = ref(store.financeDepositsProducts);

const banks = ['국민은행', '부산은행', '대구은행', '광주은행', '제주은행', '전북은행', '주식회사 케이뱅크', '한국스탠다드차타드은행', '중소기업은행', '한국산업은행', '전북은행', '주식회사 카카오뱅크', '농협은행주식회사', '토스뱅크 주식회사', '수협은행', '경남은행', '광주은행', '신한은행', '하나은행' ];

const selectedBank = ref(null);

const searchProducts = (selectedBank) => {
products.value = store.financeDepositsProducts.filter((product) => {
    return selectedBank === null || product.kor_co_nm === selectedBank;
});
};

const goDetail = (key) => {
router.push({
    name: 'DepositsDetail',
    params: { key: key },
});
};

const currentIndex = ref(0);

const visibleItems = computed(() => {
const start = currentIndex.value * 3;
const end = start + 3;
return products.value.slice(start, end);
});

const nextSlide = () => {
if (currentIndex.value < Math.ceil(products.value.length / 3) - 1) {
    currentIndex.value++;
}
};

const prevSlide = () => {
if (currentIndex.value > 0) {
    currentIndex.value--;
}
};
</script>

<style scoped>
@media (max-width: 1199px) {
/* 화면 너비가 1199px 이하일 때 */
.finance-card {
    width: 100%; /* 카드를 화면 폭에 꽉 채우도록 설정 */
}
}
/* finance-card 클래스를 활용하여 금융 데이터스러운 디자인을 적용합니다. */
.finance-card {
margin-bottom: 20px;
border: 1px solid #e2e2e2;
border-radius: 10px;
overflow: hidden;
transition: transform 0.3s;
}

.finance-card:hover {
transform: scale(1.05);
}

/* finance-table 클래스를 활용하여 테이블 스타일을 조절합니다. */
.finance-table {
margin-top: 10px;
border-collapse: collapse;
width: 100%;
}

/* 테이블 헤더 스타일 */
.finance-table th {
background-color: magenta; /* 딸기우유처럼 분홍색 */
color: white;
border: 1px solid white; /* 테두리 추가 */
border-radius: 8px; /* 모서리를 둥글게 만듦 */
padding: 10px; /* 내부 여백 추가 */
}

/* 테이블 내용 스타일 */
.finance-table td {
white-space: nowrap;
word-wrap: break-word;
border: 1px solid #ff6f96; /* 테두리 추가 */
border-radius: 8px; /* 모서리를 둥글게 만듦 */
padding: 10px; /* 내부 여백 추가 */
}

.search-title {
font-size: 1.5rem;
font-weight: bold;
color: #00376b; /* 네이버 블루 */
margin-bottom: 10px;
}
/* 추가적인 스타일링이 필요하다면 여기에 추가하세요. */
</style>
