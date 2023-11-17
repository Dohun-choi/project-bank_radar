<template>
    <div>
        <h2>DEPOSITS</h2>
        <Deposits />
        <hr>
        <!-- <h2>SAVINGS</h2>
        <Savings /> -->
    </div>
</template>

<script setup>
import Deposits from '@/components/finance/Deposits.vue';
import Savings from '@/components/finance/Savings.vue';
import { useCounterStore } from '../../stores/counter';
import { onMounted } from 'vue';

const store = useCounterStore()
onMounted(()=>{
    store.updateFinanceProducts()
    store.getFinanceDepositsProducts()
    store.getFinanceSavingsProducts()
})
</script>


<style scoped>

</style>
