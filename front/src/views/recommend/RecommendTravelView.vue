<template>
    <div>
        <button :class="{ active: isShowTerm }" @click="showTerm">{{isShowTerm? '여행지 추천 중' : '여행지 추천받기'}}</button>
        <button :class="{ active: isShowCountry }" @click="showCountry">{{isShowCountry? '적금  추천 중' : '적금 추천받기'}}</button>

        <Term v-if="isShowTerm" />
        <Country v-if="isShowCountry" />
    </div>
</template>

<script setup>
import Term from '@/components/recommend/Term.vue'
import Country from '@/components/recommend/Country.vue'
import { ref } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';

const isShowTerm = ref(true);
const isShowCountry = ref(false);

const showTerm = () => {
    isShowTerm.value = true;
isShowCountry.value = false;
};

const showCountry = () => {
    isShowTerm.value = false;
isShowCountry.value = true;
};
</script>

<style scoped>
button {
background-color: #007bff;
color: #ffffff;
padding: 10px 20px;
border: none;
cursor: pointer;
transition: background-color 0.3s ease;
}

button.active {
background-color: #0056b3;
}

button:hover {
background-color: #0056b3;
}

button + button {
margin-left: 10px;
}
</style>