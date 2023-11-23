<template>
  <div>
    <form @submit.prevent="search" class="mt-3">
      <div class="input-group">
        <label class="input-group-text" for="search">검색창:</label>
        <input type="text" id="search" v-model="search_query" class="form-control">
        <button type="submit" class="btn">검색하기</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, getCurrentInstance } from 'vue';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios'

const currentInstance = getCurrentInstance();
const store = useCounterStore()
const API_URL = store.API_URL
const search_query = ref('')

const search = () => {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/community/posts/search/`,
      params: {
        search_query: search_query.value
      },
    })
    .then((res)=>{
      console.log('검색 성공', res.data)
      currentInstance.emit('search', res.data)
      
    })
    .catch((err)=>{
      console.log('검색 실패', err)
    })
  }
</script>

<style scoped>
.btn{
  background-color: rgb(241, 125, 166);
  border-color: rgb(241, 125, 166);
  color: white;
}
</style>
