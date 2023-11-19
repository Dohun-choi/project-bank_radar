<template>
  <div>
    <table class="table table-striped">
      <thead>
        <tr class="table-primary">
          <th scope="col">idx</th>
          <th scope="col">title</th>
          <th scope="col">content</th>
          <th scope="col">updated_at</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">{{ post.id }}</th>
          <td>{{ post.title }}</td>
          <td>{{ post.content}}</td>
          <td> {{ post.updated_at }}</td>
          <!-- 게시글 좋아요 -->
          <td> 좋아요 수 : {{postLikeCount}}</td>
        </tr>
      </tbody>
      <!-- 게시글 버튼 -->
      <div>
      <button @click="deletePost">[DELETE]</button> |
      <button @click="moveModify">[MODIFY]</button> |

      <button @click="postLike">{{ isPostLike ? '[좋아요 취소]' : '[좋아요]' }}</button>

    </div>
    <hr>
    </table>
    
    <!-- 댓글관리 -->
    <div v-for="(comment, index) in post.comment_set" :key="comment.id" :showModify="comment.id">
      <div>
        <p>{{ comment.content }}</p>
        <p>좋아요 수 : {{ commentLikeCounts[index].value }}</p>
        <button @click="commentLike(comment.id, index)">
          {{ commentLikes[index].value ? '[좋아요 취소]' : '[좋아요]' }}
        </button>

        <!-- 댓글 수정 -->
        <div v-show="comment.showModify">
          <form @submit.prevent="commentModify(comment.id)">
            <label for="newContent">코멘트 변경</label>
            <input type="text" id="newContent" v-model="newContent">
            <input type="submit" value="수정하기">
          </form>
        </div>
        <button @click="comment.showModify = !comment.showModify">[mod]</button>
        <button @click="deleteComment(comment.id)">[del]</button>
    </div>
    </div>

    <div>
      <form @submit.prevent="createComment">
        <label for="comment">댓글 작성</label>
        <input type="text" id="comment" v-model="comment">
        <input type="submit" value="[댓글달기]">
      </form>
    </div>
    <button @click="log">log</button>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';
import { computed } from '@vue/reactivity';

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const post = ref('')

const comment = ref('') // 
const newContent = ref('') // 코멘트 수정
const isPostLike = ref(false) // 게시글 좋아요

const postLikeCount = ref('')
const commentLikes = ref([]) // 각 댓글의 좋아요 여부 배열
const commentLikeCounts = ref([]) // 각 댓글의 좋아요 수 배열

const log = () => {
  console.log(post.value)
}

onMounted(()=>{
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/`
})
.then((res)=>{
  post.value = res.data
  // 코멘트 각각 showModify 추가
  post.value.comment_set.forEach(e=>{e.showModify = ref(false)
  //코멘트 좋아요 여부 확인
  commentLikes.value.push(ref(e.like_users.includes(post.value.user)))
        commentLikeCounts.value.push(ref(e.like_users.length))
  })
  
  // 게시글 좋아요 여부 확인
  isPostLike.value = post.value.like_users.includes(post.value.user)
  postLikeCount.value = post.value.like_count
    })
    .catch((err) => {
      console.log(err);
    });
});

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
  console.log('성공')
  router.push({name: 'ArticleView'})
})
.catch((err)=>{
  console.log('실패', err)
}) 
}

// 수정 페이지로 이동
const moveModify = () =>
  router.push({name: 'ModifyView'})

// 댓글 달기
const createComment = () => {
  axios({
      method: 'POST',
      url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/comments/`,
      data: {content: comment.value},
      headers: {
        Authorization: `Token ${store.token}`
      }
  })
  .then((res)=>{
    console.log('성공', res.data)
    post.value.comment_set.push(res.data)
  })
  .catch((err)=>{
    console.log('실패', err)
  }) 
}


// 댓글 삭제
const deleteComment = (commentId) => {
  axios({
    method: 'DELETE',
    url: `${store.API_URL}/api/v1/community/comments/detail/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
  console.log('성공', res.data)
  const idx = post.value.comment_set.findIndex(e => e.id === commentId)
  post.value.comment_set.splice(idx, 1)
})
.catch((err)=>{
  console.log('실패', err)
}) 
}

// 댓글 수정
const commentModify = (commentId) => {
  axios({
        method: 'PUT',
        url: `${store.API_URL}/api/v1/community/comments/detail/${commentId}/`,
        data : {
            content: newContent.value
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
.then((res)=>{
    console.log('성공')
    const idx = post.value.comment_set.findIndex(e => e.id === commentId)
    post.value.comment_set[idx] = res.data
})
.catch((err)=>{
    console.log('실패', err)
}) 
}

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
    isPostLike.value = !isPostLike.value
    postLikeCount.value = res.data.likeCount
})
.catch((err)=>{
    console.log('실패', err)
}) 
}

// 댓글 좋아요
const commentLike = (commentId, index) => {
  axios({
        method: 'POST',
        url: `${store.API_URL}/api/v1/community/comments/${commentId}/likes/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
.then((res)=>{
      console.log('성공');
      commentLikes.value[index] = ref(res.data.isLiked)
      commentLikeCounts.value[index] = ref(res.data.likeCount)
})
.catch((err)=>{
    console.log('실패', err)
}) 
}



</script>

<style scoped>

</style>
