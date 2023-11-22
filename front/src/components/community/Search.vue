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
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';

const search_query = ref('')
const store = useCounterStore()
const search = () => {
  store.search(search_query.value)
}
</script>

<style scoped>
.btn{
  background-color: rgb(241, 125, 166);
  border-color: rgb(241, 125, 166);
  color: white;
}
</style>
