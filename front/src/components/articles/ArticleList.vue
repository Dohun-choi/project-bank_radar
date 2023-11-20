<template>
    <div>
      <h3>Article List</h3>
      <div>
      <RouterLink :to="{name: 'DetailView', params:{id: post.id}}">{{ post }}</RouterLink>
      <hr>
    </div>
    </div>
  </template>
  
  <script setup>
  
  import { useCounterStore } from '@/stores/counter';
  
  defineProps({
      post: Object
  })
  
  const store = useCounterStore()
  </script>
  