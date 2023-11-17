<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createPost">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';
import axios from 'axios';

const title = ref(null)
const content = ref(null)
const router = useRouter()
const store = useCounterStore()

const createPost = ()=>{
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/community/posts/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res)=>{
    console.log('성공')
    router.push({name: 'ArticleView'})
  })
  .catch((err)=>{
    console.log('실패', err)
    console.log(store.token)
  })
}


</script>

<style>

</style>
