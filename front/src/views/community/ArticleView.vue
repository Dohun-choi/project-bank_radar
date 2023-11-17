<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{name: 'CreateView'}">Create</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/articles/ArticleList.vue'
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';

const store = useCounterStore()
onMounted(()=>{
  store.getPosts()
})
</script>

<style>

</style>
