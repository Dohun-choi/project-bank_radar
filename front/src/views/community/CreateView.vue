<template>
  <div>
    <div  class="container mt-4 text-left">
    <h3 class="custom-heading">게시글 작성</h3>
    <form @submit.prevent="createPost" class="custom-form">
      <div class="mb-3">
        <label for="title" class="form-label">제목:</label>
        <input type="text" v-model.trim="title" id="title" class="form-control" maxlength="50" placeholder="제목">
        <p>{{ title.length }} / 50</p>
        <p v-if="title.length >= 50" style="color: red;">제목은 최대 50글자까지 입력가능합니다.</p>
      </div>
      <div>
        <label for="content" class="form-label">내용:</label>
        <textarea v-model.trim="content" id="content" class="form-control" placeholder="내용"></textarea>
        <p>{{ content.length }} / 1500</p>
        <p v-if="content.length >= 1500" style="color: red;">내용은 최대 1500글자까지 입력가능합니다.</p>
      </div>
      <input type="submit" class="btn btn-danger">
    </form>
</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const title = ref('')
const content = ref('')
const router = useRouter()
const store = useCounterStore()

const createPost = ()=>{
  if (title.value.length === 0) {
    return alert('제목을 입력하세요')
  } else if (title.value.length > 50) {
    return alert('제목은 최대 50글자까지 입력가능합니다.')
  } else if (content.value.length === 0) {
    return alert('내용을 입력하세요')
  } else if (content.value.length > 1500) {
    return alert('내용은 최대 1500글자까지 입력가능합니다.')
  } else {
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
}


</script>

<style>
.custom-form {
max-width: 400px;
margin: 0 auto;
}

.btn-danger {
background-color: #ff69b4; /* 딸기우유 색상 */
border-color: #ff69b4; /* 딸기우유 색상 */
}

.btn-danger:hover {
background-color: rgb(241, 125, 166); /* 진한 딸기우유 색상 */
border-color: rgb(241, 125, 166); /* 진한 딸기우유 색상 */
}
.custom-heading {
color: #ff69b4; /* 딸기우유 색상 */
margin-bottom: 1.5rem; /* 아래 여백 추가 */
}
</style>
