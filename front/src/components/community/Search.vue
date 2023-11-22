<template>
  <div>
    <form @submit.prevent="serach">
      <label for="search">검색창:</label>
      <input type="text" id="search" v-model="serach_query">
      <input type="submit" value="검색하기">
    </form>
    {{ result.value }}
  </div>
</template>

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
    data: {
      params: serach_query.value,
      serach_query: serach_query.value
    },
  })
  .then((res)=>{
    console.log('성공', res)
    result.value = res
  })
  .catch((err)=>{
    console.log('실패', err)
  })
}

</script>

<style scoped>

</style>
