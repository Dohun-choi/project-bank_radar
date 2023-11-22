<template>
  <div>
    <div  class="article-page-container">
    <h1 class="text-center mb-4">자유 게시판</h1>
    <div class="contain">
      <Search class="m-1 mb-3"/>
      <div>
        <RouterLink :to="{name: 'CreateView'}" class="btn btn-magenta mb-3 m-1">글쓰기</RouterLink>
        <button @click="popular" class="btn btn-magenta mb-3 m-1">{{ seePopular ? '인기글':'전체글' }}</button>
      </div>
    </div>

    
    <template v-if="posts !== null">
        <ArticleListItem v-for="post in posts" :key="post.id" :post="post" />
    </template>
    <template v-else>
        <p>{{ '로딩중' }}</p>
    </template>

  </div>
</div>
</template>

<script setup>
import ArticleListItem from '@/components/articles/ArticleListItem.vue'
import Search from '@/components/community/Search.vue'
import { onMounted, ref, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import axios from 'axios';

const posts = ref(null)
const store = useCounterStore()

const API_URL = store.API_URL
const token = store.token

const url = computed(() => {
  if(seePopular.value) {
    return `${API_URL}/api/v1/community/posts/popular`
  } else {
    return `${API_URL}/api/v1/community/posts/`
  }
})
const seePopular = ref(true)

onMounted(async ()=>{
    await axios({
      method: 'get',
      url : `${API_URL}/api/v1/community/posts/`,
      headers:{
        Authorization: `Token ${token}`
      }
    })
    .then((res) =>{
      console.log('성공', res)
      posts.value = res.data
    })
    .catch((err)=>{
      console.log('실패', err)
    })
})

const popular = () => {
    axios({
      method: 'get',
      url : url.value,
      headers:{
        Authorization: `Token ${token}`
      }
    })
    .then((res) =>{
      console.log('성공', res)
      posts.value = res.data
      seePopular.value = !seePopular.value
    })
    .catch((err)=>{
      console.log('실패', err)
    })
}
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