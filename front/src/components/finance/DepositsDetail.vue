<template>
    <div>
        <table class="table table-striped">
            <thead>
                <tr class="table-primary">
                <th scope="col">금융 상품명</th>
                <th scope="col">금융 회사명</th>
                <th scope="col">금융 상품 설명</th>
                <th scope="col">가입기간</th>
                <th scope="col">금리</th>
                <th scope="col">가입 방법</th>
                <th scope="col">가입 대상</th>
                <th scope="col">최고 한도</th>
                <th scope="col">우대조건</th>
                <th scope="col">좋아요(담기)</th>
                <th scope="col">눌러</th>
                

                </tr>
            </thead>
            <tbody v-for="option in product.options" :key="option.id" >
                <td>{{ product.fin_prdt_nm }}</td>
                <td>{{ product.kor_co_nm }}</td>
                <td>{{ product.etc_note }}</td>
                <td>{{ option.save_trm }}</td>
                <td>{{ option.intr_rate }}</td>
                <td>{{ product.join_way }}</td>
                <td>{{ product.join_member }}</td>
                <td>{{ formatNumber(product.max_limit) }}</td>
                <td>{{ product.spcl_cnd }}</td>
                <td >{{ productLikeCount }}</td>
                <button @click="depositsProductsLike">{{ isProductLike ? '[가입 취소]' : '[가입하기]' }}</button>
            </tbody>
            </table>
        <!-- 게시글 달기 -->
        <hr>
        <form @submit.prevent="createDebate">
            <label for="content"> 할 말 쓰기</label>
            <input type="text" id="content" v-model="content">
            <input type="submit" value="글 작성">
        </form>

        <!-- 게시글 보기 -->
        <hr>
        <h2>투기장</h2>
        <div v-for="debate in debates">
            <p>{{ debate.content }}</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';



const route = useRoute()
const store = useCounterStore()
const key = route.params.key

const debates = ref(null)
const content = ref(null)

const isProductLike = ref(null)
const productLikeCount = ref(null)

const product = store.financeDepositsProducts.find(product => product.fin_prdt_cd === key)

const formatNumber = num => new Intl.NumberFormat().format(num)

onMounted(()=>{
    // 투기장 (댓글) 불러오기
    axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/fin-product/deposits/debate/${key}/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log('성공');
    debates.value = res.data
})
.catch((err)=>{
console.log('실패', err)
}) 
})

// 게시글 생성
const createDebate = () => {
axios({
    method: 'POST',
    url: `${store.API_URL}/api/v1/fin-product/deposits/debate/${key}/`,
    data:{content: content.value},
    headers: {
        Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log('성공');
    debates.value.push(res.data)
})
.catch((err)=>{
console.log('실패', err)
}) 
}


// 구독 좋아요 알림설정
const depositsProductsLike = () => {
axios({
    method: 'POST',
    url: `${store.API_URL}/api/v1/fin-product/deposits/${key}/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log('성공');
    isProductLike.value = res.data.isLiked
    productLikeCount.value = res.data.likeCount
})
.catch((err)=>{
console.log('실패', err)
}) 
}

console.log(product)

</script>

<style scoped>

</style>
