<template>
  <div>
    <p> {{ post }}</p>

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
