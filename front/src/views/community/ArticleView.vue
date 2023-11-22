<template>
  <div class="article-page-container">
    <h1 class="text-center mb-4">게시글 페이지</h1>
    <RouterLink :to="{name: 'CreateView'}" class="btn btn-magenta mb-3">글쓰기</RouterLink>

    <Search />
    
    <ArticleList />

  </div>
</template>

<script setup>
import ArticleList from '@/components/articles/ArticleList.vue'
import Search from '@/components/community/Search.vue'
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';

const store = useCounterStore()
onMounted(()=>{
  store.getPosts()
})
</script>

<style scoped>
.article-page-container {
  max-width: 600px;
  margin: 0 auto;
}

.btn-magenta {
  background-color: #e5007e; /* Magenta color */
  border-color: #e5007e; /* Magenta color */
  color: white;
}
</style>