<template>
  <div>
    <p> {{ post.title }}</p>
    
    <RouterLink :to="{name: 'DetailView', params:{id: post.id}}">Detail</RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  post: Object,
}
)
</script>
