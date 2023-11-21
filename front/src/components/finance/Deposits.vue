<template>
    <div>
        <p>검색하기</p>
        <form @submit.prevent="searchProducts(selectedBank)">
        <!-- 은행 -->
        <select v-model="selectedBank">
            <option v-for="bank in banks" :value="bank" :key="bank">
            {{ bank }}
            </option>
        </select>
    
        <input type="submit" value="확인">
        </form>
    
        <div id="app" class="container mt-5">
        <div class="row">
            <div class="col-md-1">
            <button @click="prevSlide" class="btn btn-primary" :disabled="currentIndex === 0">이전</button>
            </div>
    
            <div class="col-md-9">
            <div class="row">
                <div v-for="(item, index) in visibleItems" :key="index" class="col-lg-4 col-md-6 col-sm-12">
                <div class="card finance-card">
                    <img @click="goDetail(item.fin_prdt_cd)" src="@/assets/eve.jpg" class="card-img-top" alt="Finance Image">
                    <div class="card-body">
                    <h5 class="card-title">{{ item.kor_co_nm }} - {{ item.fin_prdt_nm }}</h5>
                    <table class="table table-striped finance-table">
                        <thead>
                        <tr>
                            <!-- <th scope="col">금융 회사명</th> -->
                            <!-- <th scope="col">금융 상품명</th> -->
                            <!-- <th scope="col">금융 상품 설명</th> -->
                            <!-- <th scope="col">우대조건</th> -->
                            <th scope="col">공시 제출 월</th>
                            <th scope="col">가입 제한</th>
                            <th scope="col">가입 대상</th>
                            <th scope="col">가입 방법</th>
                            <th scope="col">최고한도</th>
                            <th scope="col">좋아요</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <!-- <td>{{ item.kor_co_nm }}</td> -->
                            <!-- <td>{{ item.fin_prdt_nm }}</td> -->
                            <!-- <td>{{ item.etc_note }}</td> -->
                            <!-- <td>{{ item.spcl_cnd }}</td> -->
                            <td>{{ item.dcls_month }}</td>
                            <td>{{ item.join_deny }}</td>
                            <td>{{ item.join_member }}</td>
                            <td>{{ item.join_way }}</td>
                            <td>{{ item.max_limit }}</td>
                            <td>{{ item.like_users }}</td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                </div>
                </div>
            </div>
            </div>
    
            <div class="col-md-1">
            <button @click="nextSlide" class="btn btn-primary" :disabled="currentIndex === Math.ceil(products.length / 4) - 1">다음</button>
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
    
    const banks = ['국민은행', '부산은행', '대구은행'];
    
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
    const start = currentIndex.value * 4;
    const end = start + 4;
    return products.value.slice(start, end);
    });
    
    const nextSlide = () => {
    if (currentIndex.value < Math.ceil(products.value.length / 4) - 1) {
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
    white-space: normal;
    word-wrap: break-word;
    border: 1px solid #ff6f96; /* 테두리 추가 */
    border-radius: 8px; /* 모서리를 둥글게 만듦 */
    padding: 10px; /* 내부 여백 추가 */
    }
    
    /* 추가적인 스타일링이 필요하다면 여기에 추가하세요. */
    </style>
    