<template>
    <div>
        <p>검색하기</p>
        <form @submit.prevent="searchProducts(selectedBank)">
            <!-- 은행 -->
            <select v-model="selectedBank">
                <option v-for="bank in banks" :value="bank" :key="1" >
                    {{ bank }}
                </option>
            </select>

            <input type="submit" value="확인">
        </form>
    </div>
    <div>
        <table class="table table-striped">
            <thead>
                <tr class="table-primary">
                <th scope="col">공시 제출 월</th>
                <th scope="col">금융 회사명</th>
                <th scope="col">금융 상품명</th>
                <th scope="col">금융 상품 설명</th>
                <th scope="col">가입 제한(1: 제한 없음, 2: 서민전용, 3:일부제한)</th>
                <th scope="col">가입 대상</th>
                <th scope="col">가입 방법</th>
                <th scope="col">최고한도</th>
                <th scope="col">우대조건</th>
                <th scope="col">좋아요</th>
                </tr>
            </thead>


            <tbody @click="goDetail(product.fin_prdt_cd)" v-for="product in products" :key="product.fin_prdt_cd" >
                <tr>
                    <td>{{ product.dcls_month }}</td>
                    <td>{{ product.kor_co_nm }}</td>
                    <td>{{ product.fin_prdt_nm }}</td>
                    <td>{{ product.etc_note }}</td>
                    <td>{{ product.join_deny }}</td>
                    <td>{{ product.join_member }}</td>
                    <td>{{ product.join_way }}</td>
                    <td>{{ product.max_limit }}</td>
                    <td>{{ product.spcl_cnd }}</td>
                    <td>{{ product.like_users }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useCounterStore();

const products = ref(store.financeDepositsProducts)

const banks = ['국민은행', '부산은행', '대구은행']
const periods = ['6개월', '12개월', '24개월']

const selectedBank = ref(null);



const searchProducts = (selectedBank) => {
    products.value = store.financeDepositsProducts.filter(product => {
    return (
        // 은행이 선택되지 않거나, 선택한 은행
        (selectedBank === null || product.kor_co_nm === selectedBank))
    })
}

const goDetail = (key) => {
    router.push({
        name: 'DepositsDetail',
        params:{key: key},
}
)}

</script>


<style scoped>

</style>
