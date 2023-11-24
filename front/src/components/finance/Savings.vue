<template>
    <div>
        <div class="search-form">
        <p class="search-title">검색하기</p>
        <div class="d-flex" style="display: flex; justify-content: space-between;">
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
        <button @click="btn" class="btn btn-primary ml-2">가입자순</button>
        </div>
    </div>
    
        <div>
        <table class="table table-striped table-bordered">
            <thead>
            <tr class="table-primary">
                <th scope="col">금융상품명</th>
                <th scope="col">담당은행</th>
                <th scope="col">가입제한</th>
                <th scope="col">가입대상</th>
                <th scope="col">최고한도</th>
                <th scope="col">가입자 수</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(product, index) in displayedProducts" :key="product.fin_prdt_cd" @click="goDetail(product.fin_prdt_cd)"
                :style="{ background: index % 2 === 0 ? '#f5f5f5' : '' }">
                <td>{{ product.fin_prdt_nm }}</td>
                <td>{{ product.kor_co_nm }}</td>
                <td v-if="product.join_deny === 1">-</td>
                <td v-if="product.join_deny === 2">서민 전용</td>
                <td v-if="product.join_deny === 3">일부 제한</td>
                <td>{{ product.join_member  }}</td>
                <td>{{ product.max_limit? formatNumber(product.max_limit) : '-' }} </td>
                <td>{{ product.into_count }}명</td>
            </tr>
            </tbody>
        </table>
        </div>
    
        <!-- 페이징 -->
        <nav aria-label="Page navigation">
        <ul class="pagination">
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
            <a class="page-link" href="#" aria-label="Previous" @click="changePage(currentPage - 1)">
                <span aria-hidden="true">&laquo;</span>
            </a>
            </li>
    
            <li v-for="page in pages" :key="page" class="page-item" :class="{ active: page === currentPage }">
            <a class="page-link" href="#" @click="changePage(page)">{{ page }}</a>
            </li>
    
            <li class="page-item" :class="{ disabled: currentPage === totalPages }">
            <a class="page-link" href="#" aria-label="Next" @click="changePage(currentPage + 1)">
                <span aria-hidden="true">&raquo;</span>
            </a>
            </li>
        </ul>
        </nav>
    </div>
    </template>
    
    <script setup>
    import { useCounterStore } from '@/stores/counter';
    import { ref, computed } from 'vue';
    import { useRouter } from 'vue-router';
    import 'bootstrap/dist/css/bootstrap.min.css';
    
    const router = useRouter();
    const store = useCounterStore();
    
    const formatNumber = num => new Intl.NumberFormat().format(num);
    
    const products = ref(store.financeSavingsProducts);
    const banks = ['국민은행', '부산은행', '대구은행', '광주은행', '제주은행', '전북은행', '주식회사 케이뱅크', '한국스탠다드차타드은행', '중소기업은행', '한국산업은행', '전북은행', '주식회사 카카오뱅크', '농협은행주식회사', '토스뱅크 주식회사', '수협은행', '경남은행', '광주은행', '신한은행', '하나은행' ];
    const periods = ['6개월', '12개월', '24개월', '36개월'];
    
    const origin = JSON.parse(JSON.stringify(products.value))
    const sort = ref(false)
    const btn = () => {
        sort.value = !sort.value
        if (sort.value){
        products.value = products.value.sort((a, b) => b.into_count - a.into_count);}
        else {products.value = origin}
        console.log(origin)
    }

    const selectedBank = ref(null);
    const selectedPeriod = ref(null);
    const itemsPerPage = 10; // 페이지당 아이템 수
    const currentPage = ref(1);

    
    const displayedProducts = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return products.value.slice(start, end);
    });
    
    const totalPages = computed(() => Math.ceil(products.value.length / itemsPerPage));
    
    const pages = computed(() => {
    const pagesArray = [];
    for (let i = 1; i <= totalPages.value; i++) {
        pagesArray.push(i);
    }
    return pagesArray;
    });
    
    const searchProducts = (selectedBank, selectedPeriod) => {
    products.value = store.financeSavingsProducts.filter(product => {
        return (
        // 은행이 선택되지 않거나, 선택한 은행
        (selectedBank === null || product.kor_co_nm === selectedBank)
        );
    });
    currentPage.value = 1; // 검색 시 페이지 초기화
    };
    
    const goDetail = (key) => {
    router.push({
        name: 'SavingsDetail',
        params: { key: key },
    });
    };
    
    const changePage = (page) => {
    if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page;
    }
    };
    </script>
    
    <style scoped>
    /* 추가한 스타일 */
    .pagination {
        justify-content: center;
        margin-top: 20px;
    }
        .search-form {
        margin-bottom: 20px;
        }
    
        .search-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #00376b; /* 네이버 블루 */
        margin-bottom: 10px;
        }
    
        .form-group {
        margin-bottom: 0;
        }

th {
  white-space: nowrap;
}
    </style>
    