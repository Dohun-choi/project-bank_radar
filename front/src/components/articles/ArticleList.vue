<template>
  <div class="container mt-4">
    <h3 class="mb-4">게시글 목록</h3>

    <div v-if="store.posts.length === 0" class="alert alert-info" role="alert">
      현재 게시글이 없습니다.
    </div>

    <div v-else>
      <ArticleListItem
        v-for="post in store.posts"
        :key="post.id"
        :post="post"
      />
    </div>
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/articles/ArticleListItem.vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
</script>

<style scoped>

</style>
