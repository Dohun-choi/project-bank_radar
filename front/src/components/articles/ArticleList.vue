<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem 
    v-for="post in store.posts"
    :key="post.id"
    :post="post"
    />
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/articles/ArticleListItem.vue'

import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
</script>
