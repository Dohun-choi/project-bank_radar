<template>
    <div>
        <Exchange />
        <button @click="btn">btn</button>
    </div>
</template>

<script setup>
import Exchange from '@/components/exchange/Exchange.vue';
import { useCounterStore } from '../../stores/counter';
import { onMounted } from 'vue';

const store = useCounterStore()
onMounted(()=>{
    store.updateExchange()
    store.getExchange()
})

const btn = () => {
    store.getExchange()
}
</script>

<style scoped>

</style>
