<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';

const serach_query = ref('')
const store = useCounterStore()
const result = ref('')
const serach = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/community/posts/search/`,
    params: {
      serach_query: serach_query.value
    },
  })
  .then((res)=>{
    console.log('성공')
    result.value = res
  })
  .catch((err)=>{
    console.log('실패', err)
  })
}

</script>

<template>
  <div>
    <input type="text" v-model="serach_query">
    {{ result.value }}
  </div>
</template>

<style scoped>

</style>
