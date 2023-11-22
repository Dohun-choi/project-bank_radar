<template>

    <Deposits />
    <Savings />

  </template>
  
  <script setup>
  import Deposits from '@/components/recommend/Deposits.vue';
  import Savings from '@/components/recommend/Savings.vue';
  import { ref } from 'vue';
  
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


  </style>
  