<template>
<div class="container mt-5">
    <div>
    <h2 style="color: #e5007e;">가입한 적금</h2>
    <div v-for="(savings, index) in savingsList" :key="savings.id" class="card mb-3">
        <div class="card-body">
        <p class="card-text">
            {{ index + 1 }}. (적금){{ savings.kor_co_nm }} -
            <b @click="goSavingsDetail(savings.fin_prdt_cd)" class="naver-link">
            {{ savings.fin_prdt_nm }}
            </b>
        </p>
        </div>
    </div>
    </div>

    <div>
    <h2 style="color: #e5007e;">가입한 예금</h2>
    <div v-for="(deposits, index) in depositsList" :key="deposits.id" class="card mb-3">
        <div class="card-body">
        <p class="card-text">
            {{ index + 1 }}. (예금){{ deposits.kor_co_nm }} -
            <b @click="goDepositsDetail(deposits.fin_prdt_cd)" class="naver-link">
            {{ deposits.fin_prdt_nm }}
            </b>
        </p>
        </div>
    </div>
    </div>

    <hr />

    <div class="container mt-5">
    <h2 style="color: #e5007e;">가입한 상품 금리</h2>
    <canvas ref="myChart"></canvas>
    </div>
</div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import Chart from 'chart.js/auto';
import axios from 'axios';
import { useCounterStore } from '../../stores/counter';
import { useRouter } from 'vue-router';

const store = useCounterStore();
const router = useRouter();
const savingsList = ref([]);
const depositsList = ref([]);
const myChart = ref(null);
const FinPrdtNm = ref(null);
const IntrRate = ref(null);
const IntrRate2 = ref(null);

const btn = () => {
    savingsList.value[0] += 1
    console.log(savingsList.value)
}

onMounted(async () => {
try {
const response = await axios({
method: 'GET',
url: `${store.API_URL}/accounts/user/info/`,
headers: {
    Authorization: `Token ${store.token}`,
},
});

console.log('프로필 좋아요 데이터 가져오기 성공', response.data);

depositsList.value = response.data.deposits;
savingsList.value = response.data.savings;
} catch (error) {
console.error('프로필 좋아요 데이터 가져오기 실패', error);
}
});

watch(savingsList, () => {
FinPrdtNm.value = savingsList.value.reduce((acc, cur) => {
acc.push(cur.fin_prdt_nm);
return acc;
}, []);
FinPrdtNm.value = depositsList.value.reduce((acc, cur) => {
acc.push(cur.fin_prdt_nm);
return acc;
}, FinPrdtNm.value);

IntrRate.value = savingsList.value.reduce((acc, cur) => {
acc.push(cur.intr_rate);
return acc;
}, []);
IntrRate.value = depositsList.value.reduce((acc, cur) => {
acc.push(cur.intr_rate);
return acc;
}, IntrRate.value);

IntrRate2.value = savingsList.value.reduce((acc, cur) => {
acc.push(cur.intr_rate2);
return acc;
}, []);
IntrRate2.value = depositsList.value.reduce((acc, cur) => {
acc.push(cur.intr_rate2);
return acc;
}, IntrRate2.value);

    const chartData = {
    labels: FinPrdtNm.value,
    datasets: [
    {
        label: '저축 금리',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        data: IntrRate.value,
    },
    {
        label: '최고 우대금리',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1,
        data: IntrRate2.value,
    },
    ],
    };
    const ctx = myChart.value.getContext('2d');

    new Chart(ctx, {
    type: 'bar',
    data: chartData,
    options: {
    scales: {
        y: {
        beginAtZero: true,
        },
    },
    },
    });
});



const goSavingsDetail = (key) => {
router.push({
name: 'SavingsDetail',
params: { key: key },
});
};

const goDepositsDetail = (key) => {
router.push({
name: 'DepositsDetail',
params: { key: key },
});
};
</script>

<style scoped>
body {
background-color: #f8f9fa;
}

.card-text {
font-size: 16px;
color: #333; /* 내용 색상 */
}

.naver-link {
color: #0070c0; 
cursor: pointer;
text-decoration: underline;
}
</style>
