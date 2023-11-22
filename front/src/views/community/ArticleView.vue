<template>
  <div>
    <div  class="article-page-container">
    <h1 class="text-center mb-4">자유 게시판</h1>
    <div class="contain">
      <Search />
      <RouterLink :to="{name: 'CreateView'}" class="btn btn-magenta mb-3">글쓰기</RouterLink>
    </div>

    
    <ArticleList />

  </div>
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
  max-width: 100%;
  margin: 0 auto;
}

.btn-magenta {
  background-color: rgb(241, 125, 166);
  border-color: rgb(241, 125, 166);
  color: white;
}
.contain{
  display: flex;
  justify-content: space-between;
}
</style>