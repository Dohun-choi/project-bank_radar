<template>
    <div>
        <table class="table table-striped">
            <thead>
                <tr class="table-primary">
                <th scope="col">금융 상품명</th>
                <th scope="col">금융 회사명</th>
                <th scope="col">금융 상품 설명</th>
                <th scope="col">가입기간</th>
                <th scope="col">기본 금리</th>
                <th scope="col">최대 금리</th>
                <th scope="col">금리 형식</th>

                <th scope="col">좋아요 수(명)</th>
                <th scope="col">좋아요(가입)</th>
                

                </tr>
            </thead>
            <tbody v-for="option in options" :key="option.id" >
                <td>{{ product.fin_prdt_nm }}</td>
                <td>{{ product.kor_co_nm }}</td>
                <td>{{ product.etc_note }}</td>
                <td>{{ option.save_trm }}</td>
                <td>{{ option.intr_rate }}</td>
                <td>{{ option.intr_rate2 }}</td>
                <td>{{ option.intr_rate_type_nm}}</td>
                <td>{{ option.into_count}}</td>
                <button @click="depositsProductsLike(option)">{{ option.is_into ? '[가입 취소]' : '[가입하기]' }}</button>
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

const debates = ref([])
const content = ref(null)



const product = store.financeDepositsProducts.find(product => product.fin_prdt_cd === key)
const options = ref(null)
const formatNumber = num => new Intl.NumberFormat().format(num)

onMounted(()=>{
    // 옵션 가져오기
    axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/fin-product/options/deposits/${key}/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log('옵션 가져오기 성공', res.data)
    options.value = res.data
})
.catch((err)=>{
console.log('옵션 가져오기 실패', err)
}) 

    // 투기장 (댓글) 불러오기
    axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/fin-product/deposits/debate/${key}/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log('투기장 불러오기 성공');
    debates.value = res.data
})
.catch((err)=>{
console.log('투기장 불러오기 실패', err)
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
    console.log('투기장 성공');
    if (debates.value === null){
        debates.value === res.data
    }
    else{debates.value.push(res.data)}
    
})
.catch((err)=>{
console.log('투기장 실패', err)
}) 
}


// 구독 좋아요 알림설정
const depositsProductsLike = (option) => {
axios({
    method: 'POST',
    url: `${store.API_URL}/api/v1/fin-product/deposits/${option.id}/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
    console.log('가입 성공', res.data);
    option.is_into = res.data.isLiked
    option.into_count = res.data.likeCount
})
.catch((err)=>{
console.log('가입 실패', err)
}) 
}


</script>

<style scoped>

</style>
