<template>
<div>
    <div class="product-details">
    <h3 class="product-title">{{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</h3>
    <p class="product-description">{{ product.etc_note }}</p>
    </div>

    <table class="table table-striped">
    <thead>
        <tr class="table-primary">
        <th scope="col">구분</th>
        <th scope="col">가입기간</th>
        <th scope="col">기본 금리</th>
        <th scope="col">최대 금리</th>
        <th scope="col">금리 형식</th>
        <th scope="col">좋아요 수</th>
        <th scope="col">좋아요(가입)</th>
        </tr>
    </thead>
    <tbody v-for="(option, index) in options" :key="option.id">
        <tr>
        <td>{{ index + 1 }}</td>
        <td>{{ option.save_trm }}개월</td>
        <td>{{ option.intr_rate }}%</td>
        <td>{{ option.intr_rate2 }}%</td>
        <td>{{ option.intr_rate_type_nm }}</td>
        <td>{{ option.into_count }}명</td>
        <td>
            <button @click="depositsProductsLike(option)" class="btn btn-custom">
            {{ option.is_into ? '가입 취소' : '가입하기' }}
            </button>
        </td>
        </tr>
    </tbody>
    </table>

    <!-- 게시글 달기 -->
    <hr />
    <form @submit.prevent="createDebate" class="mb-4">
    <label for="content" class="form-label">할 말 쓰기</label>
    <input type="text" id="content" v-model="content" class="form-control">
    <button type="submit" class="btn btn-custom mt-2">글 작성</button>
    </form>

    <!-- 게시글 보기 -->
    <hr />
    <div class="debates-container p-4 border rounded bg-light">
    <h2 class="text-success font-weight-bold mb-4">투기장</h2>
    <div v-for="(debate, index) in debates" :key="debate.id" class="card mb-3 w-100">
        <div class="card-body">
        <p class="card-text">{{ index + 1 }}. {{ debate.content }}</p>
        </div>
    </div>
    </div>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const route = useRoute();
const store = useCounterStore();
const key = route.params.key;

const debates = ref([]);
const content = ref(null);

const product = store.financeDepositsProducts.find((product) => product.fin_prdt_cd === key);
const options = ref(null);
const formatNumber = (num) => new Intl.NumberFormat().format(num);

onMounted(() => {
// 옵션 가져오기
axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/fin-product/options/deposits/${key}/`,
    headers: {
    Authorization: `Token ${store.token}`,
    },
})
    .then((res) => {
    console.log('옵션 가져오기 성공', res.data);
    options.value = res.data;
    })
    .catch((err) => {
    console.log('옵션 가져오기 실패', err);
    });

// 투기장 (댓글) 불러오기
axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/fin-product/deposits/debate/${key}/`,
    headers: {
    Authorization: `Token ${store.token}`,
    },
})
    .then((res) => {
    console.log('투기장 불러오기 성공');
    debates.value = res.data;
    })
    .catch((err) => {
    console.log('투기장 불러오기 실패', err);
    });
});

// 게시글 생성
const createDebate = () => {
axios({
    method: 'POST',
    url: `${store.API_URL}/api/v1/fin-product/deposits/debate/${key}/`,
    data: { content: content.value },
    headers: {
    Authorization: `Token ${store.token}`,
    },
})
    .then((res) => {
    console.log('투기장 성공');
    if (debates.value === null) {
        debates.value = res.data;
    } else {
        debates.value.push(res.data);
    }
    })
    .catch((err) => {
    console.log('투기장 실패', err);
    });
};

// 구독 좋아요 알림설정
const depositsProductsLike = (option) => {
axios({
    method: 'POST',
    url: `${store.API_URL}/api/v1/fin-product/deposits/${option.id}/`,
    headers: {
    Authorization: `Token ${store.token}`,
    },
})
    .then((res) => {
    console.log('가입 성공', res.data);
    option.is_into = res.data.isLiked;
    option.into_count = res.data.likeCount;
    })
    .catch((err) => {
    console.log('가입 실패', err);
    });
};
</script>

<style scoped>
/* 추가한 스타일 */
.btn-custom {
background-color: #4a90e2; /* 네이버 블루와 유사한 색상 */
color: #ffffff; /* 텍스트 색상을 흰색으로 설정 */
border: 1px solid #4a90e2; /* 테두리를 설정하고, 네이버 블루와 동일한 색상으로 설정 */
}

.btn-custom:hover {
background-color: #0056b3; /* 마우스 오버시 색상 변경 */
border-color: #0056b3;
}

.form-label {
font-size: 1rem; /* 폼 레이블의 글꼴 크기를 설정 */
color: #4a90e2; /* 네이버 블루와 유사한 색상 */
}

.form-control {
border: 1px solid #4a90e2; /* 폼 입력의 테두리를 설정하고, 네이버 블루와 동일한 색상으로 설정 */
}

.form-control:focus {
border-color: #0056b3; /* 입력란에 포커스 시 색상 변경 */
}

.debates-container {
display: flex;
flex-direction: column;
align-items: flex-start;
}

.card {
width: 100%;
margin-bottom: 20px;
}

.product-details {
padding: 20px;
border: 1px solid #ddd;
border-radius: 10px;
margin-bottom: 5px;
background-color: #fff;
width: 100%;
}

.product-title {
color: #e5007e; /* Magenta color */
font-size: 24px;
font-weight: bold;
margin-bottom: 10px;
}

.product-description {
color: #333;
font-size: 16px;
margin-top: 10px;
}

/* 투기장 타이틀 스타일 */
h2.text-success {
font-size: 2.5rem;
margin-bottom: 1rem;
}
</style>