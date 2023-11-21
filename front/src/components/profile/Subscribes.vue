<template>
<div>
    <div>
    <h2>가입한 적금</h2>
    <div v-for="(savings, index) in savingsList" :key="savings.id">
        <p>
        {{ index + 1 }} : (정기예금){{ savings.kor_co_nm }} -
        <b @click="goSavingsDetail(savings.fin_prdt_cd)">
            {{ savings.fin_prdt_nm }}
        </b>
        </p>
    </div>

    <h2>가입한 예금</h2>
    <div v-for="(deposits, index) in depositsList" :key="deposits.id">
        <p>
        {{ index + 1 }} : (정기예금){{ deposits.kor_co_nm }} -
        <b @click="goDepositsDetail(deposits.fin_prdt_cd)">
            {{ deposits.fin_prdt_nm }}
        </b>
        </p>
    </div>
    </div>

    <hr />
    <h2>가입한 상품 금리</h2>
    <canvas ref="myChart"></canvas>
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
const FinPrdtNm = ref(null)
const IntrRate = ref(null)
const IntrRate2 = ref(null)

onMounted(async () => {
try {
    // 프로필 좋아요 데이터 가져오기
    const response = await axios({
    method: 'GET',
    url: `${store.API_URL}/accounts/user/info/`,
    headers: {
        Authorization: `Token ${store.token}`,
    },
    });

    console.log('프로필 좋아요 데이터 가져오기 성공', response.data);

    // 비동기 작업이 완료된 후에 데이터를 업데이트

    savingsList.value = 
    // [
    //     {id: 1, kor_co_nm: '싸피은행', fin_prdt_nm : '행복행복적금', intr_rate: 3.56, intr_rate2: 3.88},
    //     {id: 2, kor_co_nm: '달수은행', fin_prdt_nm : '수달수달예금', intr_rate: 4.44, intr_rate2: 4.55},
    //     {id: 2, kor_co_nm: '말이은행', fin_prdt_nm : '이브이브이브이', intr_rate: 3.33, intr_rate2: 5.55}
    // ]
    depositsList.value = response.data.deposits;
    savingsList.value = response.data.savings;

} catch (error) {
    console.error('프로필 좋아요 데이터 가져오기 실패', error);
}
});

watch(savingsList, () =>{
    // FinprdtNm
    FinPrdtNm.value = savingsList.value.reduce((acc, cur) => {
    acc.push(cur.fin_prdt_nm);
    return acc;
    }, []);
    FinPrdtNm.value = depositsList.value.reduce((acc, cur) => {
    acc.push(cur.fin_prdt_nm);
    return acc;
    }, FinPrdtNm.value);
    
    // IntrRate
    IntrRate.value = savingsList.value.reduce((acc, cur) => {
        acc.push(cur.intr_rate);
        return acc;
    }, [])
    IntrRate.value = depositsList.value.reduce((acc, cur) => {
        acc.push(cur.intr_rate);
        return acc;
    }, IntrRate.value)

    // IntrRate2
    IntrRate2.value = savingsList.value.reduce((acc, cur) => {
        acc.push(cur.intr_rate2);
        return acc;
    }, [])
    IntrRate2.value = depositsList.value.reduce((acc, cur) => {
        acc.push(cur.intr_rate2);
        return acc;
    }, IntrRate2.value)

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
})

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

</style>

