<template>
    <div>
        <div>
            <h2 @click="viewDeposits">DEPOSITS</h2>         
            <h2 @click="ViewSavings">SAVINGS</h2>
        </div>

        <div v-if="isSavingsView">
            <Savings />
        </div>
        <div v-if="isDepositsView">
            <Deposits />
        </div>
    </div>
</template>

<script setup>
import Deposits from '@/components/finance/Deposits.vue';
import Savings from '@/components/finance/Savings.vue';
import { useCounterStore } from '../../stores/counter';
import { ref, onMounted } from 'vue';

const store = useCounterStore()
onMounted(()=>{
    store.updateFinanceProducts()
    store.getFinanceDepositsProducts()
    store.getFinanceSavingsProducts()
})

const viewDeposits = () => {
    isDepositsView.value = true
    isSavingsView.value = false
}

const ViewSavings = () => {
    isDepositsView.value = false
    isSavingsView.value = true
}

const isDepositsView = ref(true)

const isSavingsView = ref(false)

</script>


<style scoped>

</style>
