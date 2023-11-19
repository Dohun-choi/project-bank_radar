<template>
<div>
    <!-- <p> {{ profileLikes }}</p> -->
    <!-- <p> {{ profileLikes }}</p> -->
    <button @click="store.getProfileLikes">btn</button>
    <canvas ref="myChart"></canvas>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';
import { useCounterStore } from '../../stores/counter';

const store = useCounterStore()
const profileLikes = store.profileLikes

onMounted(()=>{
    store.getProfileLikes
});



const chartData = ref({
labels: ['데이터1', '데이터2', '데이터3', '데이터4'],
datasets: [
    {
    label: '데이터셋 1',
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1,
    data: [12, 19, 3, 5],
    },
    {
    label: '데이터셋 2',
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1,
    data: [8, 15, 7, 11],
    },
],
});

const myChart = ref(null);

onMounted(() => {
renderChart();
});

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
</script>

<style scoped>
/* 스타일을 추가하거나 수정할 수 있습니다. */
</style>
