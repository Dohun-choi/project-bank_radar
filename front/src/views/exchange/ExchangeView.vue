<template>
    <div>
        <Exchange />
    </div>
</template>

<script setup>
import Exchange from '@/components/exchange/Exchange.vue';
import { useCounterStore } from '../../stores/counter';
import { onMounted } from 'vue';

const store = useCounterStore()
onMounted(()=>{
    store.getExchange()
})

</script>

<style scoped>

</style>
