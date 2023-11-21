<template>
  <div>
    <table class="table table-striped">
      <thead>
        <tr class="table-primary">
          <th scope="col">idx</th>
          <th scope="col">title</th>
          <th scope="col">content</th>
          <th scope="col">updated_at</th>
          <th scope="col">좋아요</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ post.id }}</td>
          <td>{{ post.title }}</td>
          <td>{{ post.content}}</td>
          <td> {{ post.updated_at }}</td>
          <!-- 게시글 좋아요 -->
          <td> {{post.like_count}}</td>
        </tr>
      </tbody>
      <!-- 게시글 버튼 -->
      <div>
      <button @click="deletePost">[DELETE]</button> |
      <button @click="moveModify">[MODIFY]</button> |

      <button @click="postLike">{{ post.is_liked ? '[좋아요 취소]' : '[좋아요]' }}</button>
        <Comments />
    </div>
    <hr>
    </table>
    
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';
import Comments from '@/components/community/Comments.vue';

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const post = ref([])

onMounted(()=>{
  axios({
      method: 'GET',
      url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/`,
      headers: {
          Authorization: `Token ${store.token}`
      }
    })
  .then((res)=>{
      console.log('게시글 세부 정보 가져오기 성공', res.data)
      post.value = res.data
  })
  .catch((err)=>{
      console.log('게시글 세부 정보 가져오기 실패', err)
  }) 
})

// 게시글 삭제하기
const deletePost = () => {
  axios({
    method: 'DELETE',
    url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
  console.log('게시글 삭제 성공')
  router.push({name: 'ArticleView'})
})
.catch((err)=>{
  console.log('게시글 삭제 실패', err)
}) 
}

// 수정 페이지로 이동
const moveModify = () =>
  router.push({name: 'ModifyView'})


// 게시글 좋아요
const postLike = () => {
  axios({
        method: 'POST',
        url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/likes/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
.then((res)=>{
    console.log('성공')
    post.value.is_liked = res.data.isLiked
    post.value.like_count = res.data.likeCount
})
.catch((err)=>{
    console.log('실패', err)
}) 
}

</script>

<style scoped>

</style>