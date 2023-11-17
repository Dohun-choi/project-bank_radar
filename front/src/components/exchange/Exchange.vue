<template>
<div>
    <h1>환율계산기</h1>

    <div>
    <p>기준(보유)국가 - 선택한 국가 : {{ country1.cur_nm }}</p>
    <select v-model="country1">
        <option v-for="exchange in store.exchanges" :value="exchange" :key="exchange.cur_unit">
        {{ exchange.cur_nm }}
        </option>
    </select>
    </div>

    <div>
    <p>바꿀 국가 선택 - 선택한 국가 : {{ country2.cur_nm }}</p>
    <select v-model="country2">
        <option v-for="exchange in store.exchanges" :value="exchange" :key="exchange.cur_unit">
        {{ exchange.cur_nm }}
        </option>
    </select>

    <!-- 각 국가의 환율 단위에 따라 다르게 표시 -->
    <input type="text" v-model="price" @input="calculatePrice" placeholder='금액'>
    </div>

    <div>
    <textarea v-model="resPrice" readonly></textarea>
    </div>

</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';

const store = useCounterStore();

const calculatePrice = () => {
if (price.value && country1.value && country2.value) {
    let rate1 = parseFloat(country1.value.deal_bas_r)
    let rate2 = parseFloat(country2.value.deal_bas_r)
    // console.log(country1.value.cur_unit, rate1)
    // console.log(country2.value.cur_unit, rate2)
    if(country1.value.cur_unit === 'JPY(100)' || 'IDR(100)'){
        rate1 = rate1 / 100
    }
    if(country2.value.cur_unit === 'JPY(100)' || 'IDR(100)'){
        rate2 = rate2 / 100
    }
    const convertedPrice = rate1 *(price.value / rate2)

    resPrice.value = convertedPrice.toFixed(2);
}
};

console.log(store.exchanges)

const country1 = ref('');
const country2 = ref('');
const price = ref('');
const resPrice = ref('');
</script>

<style scoped>

</style>
