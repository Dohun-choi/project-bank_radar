<template>
    <div>
        <Savings />
    </div>
</template>

<script setup>
import Savings from '@/components/finance/Savings.vue';
import { useCounterStore } from '../../stores/counter';
import { onMounted } from 'vue';

const store = useCounterStore()
onMounted(()=>{
    store.updateFinanceProducts()
    store.getFinanceSavingsProducts()
})



</script>


<style scoped>

</style>
