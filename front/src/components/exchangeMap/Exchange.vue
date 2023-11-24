<template>
<div class="container mt-5">
    <h1 class="text-center mb-4">환율 계산기</h1>

    <div class="row mb-3">
    <div class="col-md-6">
        <p class="mb-2 text-muted">기준(보유) 국가 - 선택한 국가 : {{ country1.cur_nm }}</p>
        <select class="form-select" v-model="country1">
        <option v-for="exchange in store.exchanges" :value="exchange" :key="exchange.cur_unit">
            {{ exchange.cur_nm }}
        </option>
        </select>
    </div>

    <div class="col-md-6">
        <p class="mb-2 text-muted">바꿀 국가 선택 - 선택한 국가 : {{ country2.cur_nm }}</p>
        <select class="form-select" v-model="country2">
        <option v-for="exchange in store.exchanges" :value="exchange" :key="exchange.cur_unit">
            {{ exchange.cur_nm }}
        </option>
        </select>
    </div>
    </div>

    <div class="row">
    <div class="col-md-6 mb-3">
        <p class="mb-2 text-muted">환율 계산</p>
        <div class="input-group">
        <input type="text" class="form-control" v-model="price" @input="calculatePrice" placeholder="금액">
        </div>
        <p v-if="isNaN(price)">숫자를 입력하세요.</p>
    </div>

    <div class="col-md-6 mt-4">
        <p class="mb-2 text-muted">환율 결과</p>
        <textarea class="form-control" v-model="resPrice" readonly></textarea>
    </div>
    </div>
</div>

<GoogleMap :country="country2"/>


</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import GoogleMap from './GoogleMap.vue';

const store = useCounterStore();

const calculatePrice = () => {
if (price.value && country1.value && country2.value) {
    let rate1 = parseFloat(country1.value.deal_bas_r);
    let rate2 = parseFloat(country2.value.deal_bas_r);

    if (country1.value.cur_unit === 'JPY(100)' || country1.value.cur_unit === 'IDR(100)') {
    rate1 = rate1 / 100;
    }

    if (country2.value.cur_unit === 'JPY(100)' || country2.value.cur_unit === 'IDR(100)') {
    rate2 = rate2 / 100;
    }

    const convertedPrice = rate1 * (price.value / rate2);
    resPrice.value = convertedPrice.toFixed(2);
}
};

const country1 = ref('');
const country2 = ref('');
const price = ref('');
const resPrice = ref('');
</script>

<style scoped>
body {
background-color: #f8f9fa;
}

.container {
background-color: #ffffff;
border-radius: 10px;
box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
padding: 20px;
}

h1 {
color: #00376b;
}

select,
input,
textarea {
margin-top: 5px;
}

.text-muted {
color: #6c757d 
}

.form-select,
.form-control {
border: 1px solid #ced4da;
border-radius: 5px;
}

textarea {
resize: none;
}

</style>
