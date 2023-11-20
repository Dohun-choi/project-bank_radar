<template>
<div>
    <div >
        <h2>가입한 적금</h2>
        <div v-for="(savings, index) in savingsList" :key=savings.id>
            <p>{{index + 1}} : (정기예금){{ savings.kor_co_nm }} - <b @click="goSavingsDetail(savings.fin_prdt_cd)">{{savings.fin_prdt_nm}}</b></p>
        </div>

        <h2>가입한 예금</h2>
        <div v-for="(deposits, index) in depositsList" :key=deposits.id>
            <p>{{index + 1}} : (정기예금){{ deposits.kor_co_nm }} - <b @click="goDepositsDetail(deposits.fin_prdt_cd)">{{deposits.fin_prdt_nm}}</b></p>
        </div>
    </div>


    <hr>
    <h2>가입한 상품 금리</h2>
    <canvas ref="myChart"></canvas>

</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';
import { useCounterStore } from '../../stores/counter';
import { useRouter } from 'vue-router';

const store = useCounterStore()
const router = useRouter()
const savingsList = store.profileLikes.savings
const depositsList = store.profileLikes.deposits


onMounted(() => {
    store.getProfileLikes()
    renderChart();
});

// FinprdtNm = savings + deposits
const savingsFinPrdtNm =  savingsList.reduce((acc, cur)=>{
    acc.push(cur.fin_prdt_nm)
    return acc
}, [] )
const FinPrdtNm = depositsList.reduce((acc, cur)=>{
    acc.push(cur.fin_prdt_nm)
    return acc
}, savingsFinPrdtNm )


// IntrRate = savings + deposits
const savingsIntrRate = savingsList.reduce((acc, cur)=>{
    acc.push(cur.intr_rate)
    return acc
}, [] )
const IntrRate = depositsList.reduce((acc, cur)=>{
    acc.push(cur.intr_rate)
    return acc
}, savingsIntrRate )

// IntrRate2 = savings + deposits
const savingsIntrRate2 = savingsList.reduce((acc, cur)=>{
    acc.push(cur.intr_rate2)
    return acc
}, [] )
const IntrRate2 = depositsList.reduce((acc, cur)=>{
    acc.push(cur.intr_rate)
    return acc
}, savingsIntrRate2 )



const chartData = ref({
labels: FinPrdtNm,
datasets: [
    {
    label: '저축 금리',
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1,
    data: IntrRate,
    },
    {
    label: '최고 우대금리',
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1,
    data: IntrRate2,
    },
],
});

const myChart = ref(null);

const renderChart = () => {
const ctx = myChart.value.getContext('2d');
new Chart(ctx, {
    type: 'bar',
    data: chartData.value,
    options: {
    scales: {
        y: {
        beginAtZero: true,
        },
    },
    },
});
};

const goSavingsDetail = (key) => {
    router.push({
        name: 'SavingsDetail',
        params:{key: key},
}
)}

const goDepositsDetail = (key) => {
    router.push({
        name: 'DepositsDetail',
        params:{key: key},
}
)}
</script>

<style scoped>

</style>
