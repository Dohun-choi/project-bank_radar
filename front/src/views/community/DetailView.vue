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
          <td> 좋아요 수 : {{post.like_count}}</td>
        </tr>
      </tbody>
      <!-- 게시글 버튼 -->
      <div>
      <button @click="deletePost">[DELETE]</button> |
      <button @click="moveModify">[MODIFY]</button> |

      <button @click="postLike">{{ post.is_liked ? '[좋아요 취소]' : '[좋아요]' }}</button>

    </div>
    <hr>
    </table>
    
    <!-- 댓글관리 -->
    <div v-for="comment in post.comment_set" :key="comment.id" :showModify="comment.id">
      <div>
        <p>{{ comment.content }}</p>
        <p>좋아요 수 : {{ comment.like_count }}</p>
        <button @click="commentLike(comment.id, comment)">
          {{ comment.is_liked ? '[좋아요 취소]' : '[좋아요]' }}
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
        <!-- 댓글 삭제 -->
        <button @click="deleteComment(comment.id)">[del]</button>
        
        <!-- 대댓글 -->
        <div v-for="children in comment.children" :key="children.id" >
          <p> {{ children.content }}</p>
        </div>
        <div v-show="comment.showReComment">
          <form @submit.prevent="createReComment(comment.id, comment)">
            <label for="reComment">대댓글 달기</label>
            <input type="text" id="reComment" v-model="reComment">
            <input type="submit" value="작성">
          </form>
        </div>
          <button @click="comment.showReComment = !comment.showReComment">[reple]</button>
        
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

const reComment = ref('') // 대댓글

const postLikeCount = ref('')

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
  // 코멘트 각각 showModify, showReComment 추가
  post.value.comment_set.forEach(e=>{
    e.showModify = ref(false)
    e.showReComment = ref(false)
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

/// 대댓글
const createReComment = (commentId, comment) => {
  axios({
      method: 'POST',
      url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/comments/`,
      data: {
        content: reComment.value,
        parent: commentId,
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
  })
  .then((res)=>{
    console.log('대댓글 성공', res.data)
    comment.children.push(res.data)
  })
  .catch((err)=>{
    console.log('대댓글 실패', err)
  }) 
}


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
    post.value.is_liked = res.data.isLiked
    post.value.like_count = res.data.likeCount
})
.catch((err)=>{
    console.log('실패', err)
}) 
}

// 댓글 좋아요
const commentLike = (commentId, comment) => {
  axios({
        method: 'POST',
        url: `${store.API_URL}/api/v1/community/comments/${commentId}/likes/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
.then((res)=>{
      console.log(comment)
      console.log('댓글 좋아요 성공');
      comment.is_liked = ref(res.data.isLiked)
      comment.like_count = ref(res.data.likeCount)
      console.log(comment)
})
.catch((err)=>{
    console.log('실패', err)
}) 
}



</script>

<style scoped>

</style>