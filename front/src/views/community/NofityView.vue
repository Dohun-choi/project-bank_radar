<template>
    <div>
        <div v-if="notifys.length === 0">알람이 없습니다.</div>
        <div v-for="(notify) in notifys.slice().reverse()" :key=notify.id >
            <p :class="{read : notify.read===true }">content : {{ notify.content }}</p>
            <button @click="deleteNotify(notify.id)"> 삭제</button>
            <hr>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';

const store = useCounterStore()

const notifys = ref([])

onMounted(() => {
    axios({
        method: 'PUT',
        url: `${store.API_URL}/api/v1/community/notify/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log('notify 데이터 가져오기 성공', res.data);
        notifys.value = res.data
    })
    .catch((err)=>{
    console.log('notify 가져오기 실패', err)
    })
});

const deleteNotify = (notifyId) => {
    axios({
        method: 'DELETE',
        url: `${store.API_URL}/api/v1/community/notify/${notifyId}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        console.log('notify delete 성공');
        notifys.value = notifys.value.filter((a) => a.id !== notifyId)
    })
    .catch((err)=>{
    console.log('notify delete 실패', err)
    })
}
</script>

<style scoped>
.read {
    color: gainsboro;
}
</style>