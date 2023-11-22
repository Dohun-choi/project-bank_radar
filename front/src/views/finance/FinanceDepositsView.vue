<template>
    <div>
        <Deposits />
    </div>
</template>

<script setup>
import Deposits from '@/components/finance/Deposits.vue';
import { useCounterStore } from '../../stores/counter';
import {  onMounted } from 'vue';

const store = useCounterStore()
onMounted(()=>{
    store.updateFinanceProducts()
    store.getFinanceDepositsProducts()
})


</script>


<style scoped>

</style>
