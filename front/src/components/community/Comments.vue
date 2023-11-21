<template>
    <div>
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
  import { useRoute } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';
  import 'bootstrap/dist/css/bootstrap.min.css';
  
  const store = useCounterStore()
  const route = useRoute()
  const post = ref('')
  const comment = ref('') // 
  const newContent = ref('') // 코멘트 수정
  const reComment = ref('') // 대댓글
  
  
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
    })
    .catch((err) => {
        console.log(err);
    });
  });
  

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
      console.log('댓글 작성 성공', res.data)
      console.log(post.value.comment_set)
      post.value.comment_set.push(res.data)
    })
    .catch((err)=>{
      console.log('댓글 작성 실패', err)
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