<template>
    <div>
        <p>검색하기</p>
        <form @submit.prevent="searchProducts(selectedBank, selectedPeriod)">
            <!-- 은행 -->
            <select v-model="selectedBank">
                <option v-for="bank in banks" :value="bank" :key="1" >
                    {{ bank }}
                </option>
            </select>
            <!-- 예치기간 -->
            <!-- <select v-model="selectedPeriod">
                <option v-for="period in periods" :value="period" :key="1">
                    {{ period }}
                </option>
            </select> -->

            <input type="submit" value="확인">
        </form>
    </div>
    <div>
        <table class="table table-striped">
            <thead>
                <tr class="table-primary">
                <th scope="col">금융상품명</th>
                <th scope="col">담당은행</th>
                <th scope="col">가입제한</th>
                <th scope="col">최고한도(원)</th>

                </tr>
            </thead>
            <tbody @click="goDetail(product.fin_prdt_cd)" v-for="product in products" :key="product.fin_prdt_cd" >
                    <td>{{ product.fin_prdt_nm }}</td>
                    <td>{{ product.kor_co_nm }}</td>
                    
                    <td v-if="product.join_deny === 1">제한 없음</td>
                    <td v-if="product.join_deny === 2">서민 전용</td>
                    <td v-if="product.join_deny === 3">일부 
                    제한</td>
                    
                    <td>{{ formatNumber(product.max_limit) }}</td>
            </tbody>
            
        </table>
    </div>
    <button @click="log">gd</button>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const log = ()=>{
    console.log(products.value[0].options.intr_rate)
    console.log(products.value)}

const store = useCounterStore();

const formatNumber = num => new Intl.NumberFormat().format(num)
const products = ref(store.financeSavingsProducts)

const banks = ['국민은행', '부산은행', '대구은행', '광주은행', '제주은행', '전북은행']
const periods = ['6개월', '12개월', '24개월, 36개월']

const selectedBank = ref(null);
const selectedPeriod = ref(null);


const searchProducts = (selectedBank, selectedPeriod) => {
    products.value = store.financeSavingsProducts.filter(product => {
    return (
        // 은행이 선택되지 않거나, 선택한 은행
        (selectedBank === null || product.kor_co_nm === selectedBank))})
}

const goDetail = (key) => {
    router.push({
        name: 'SavingsDetail',
        params:{key: key},
}
)}
</script>


<style scoped>

</style>
