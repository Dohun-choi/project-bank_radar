<template>
    <div>
        <h2>Notify</h2>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';

const store = useCounterStore()

const notifys = ref(null)

onMounted(() => {
    axios({
        method: 'PUT',
        url: `${store.API_URL}/api/v1/community/notify/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log('notify 가져오기 성공', res.data);
        notifys.value = res.data
    })
    .catch((err)=>{
    console.log('notify 가져오기 실패', err)
    })
});

const deleteNotify = (notifyPk) => {
    axios({
        method: 'DELETE',
        url: `${store.API_URL}/api/v1/community/notify/${notifyPk}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log('notify delete 성공');
    })
    .catch((err)=>{
    console.log('notify delete 실패', err)
    })
}
</script>

<style scoped>

</style>