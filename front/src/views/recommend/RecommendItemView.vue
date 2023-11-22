<template>
  <div>
    <button :class="{ active: isShowDeposits }" @click="showDeposits">{{isShowDeposits? '예금  추천 중' : '예금 추천받기'}}</button>
    <button :class="{ active: isShowSavings }" @click="showSavings">{{isShowSavings? '적금  추천 중' : '적금 추천받기'}}</button>

    <Deposits v-if="isShowDeposits" />
    <Savings v-if="isShowSavings" />
  </div>
</template>
  
  <script setup>
  import Deposits from '@/components/recommend/Deposits.vue';
  import Savings from '@/components/recommend/Savings.vue';
  import { ref } from 'vue';
  import 'bootstrap/dist/css/bootstrap.min.css';
  
  const isShowDeposits = ref(true);
  const isShowSavings = ref(false);
  
  const showDeposits = () => {
    isShowDeposits.value = true;
    isShowSavings.value = false;
  };
  
  const showSavings = () => {
    isShowDeposits.value = false;
    isShowSavings.value = true;
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
  