<template>
  <div>

    <!-- 댓글 작성 -->
    <div class="create-comment">
      <form @submit.prevent="createComment">
        <label for="comment" class="form-label"><strong>댓글 작성</strong></label>
        <div >
          <input type="text" id="comment" v-model="comment" class="form-control" placeholder="댓글을 입력해주세요.">
          <button type="submit" class="btn btn-primary ml-2">댓글달기</button>
        </div>
      </form>
    </div>
    <hr>

    <!-- 댓글 관리 -->
    <div v-for="(comment, index) in post.comment_set" :key="comment.id" :showModify="comment.id">
      <div class="comment-container card mb-3">
        <div class="card-body">
          <p class="card-text comment-content">
              <!-- 댓글 번호 -->
              <b class="comment-number comment-content">#{{ index + 1 }}</b>
              {{ comment.content }}
          </p>
          <p class="card-text like-count">좋아요 : {{ comment.like_count }} 개</p>
          <button @click="commentLike(comment.id, comment)" class="btn btn-primary">
            {{ comment.is_liked ? '좋아요 취소' : '좋아요' }}
          </button>

          <!-- 댓글 수정 -->
          <div v-show="comment.showModify" class="modify-comment">
            <form @submit.prevent="commentModify(comment.id)">
              <label for="newContent" class="form-label">댓글 수정</label>
              <input type="text" id="newContent" v-model="newContent" class="form-control">
              <button type="submit" class="btn btn-warning ml-2">수정하기</button>
            </form>
          </div>
          <button @click="comment.showModify = !comment.showModify" class="btn btn-secondary ml-2">{{comment.showModify? '접기' : '수정하기'}}</button>
          <!-- 댓글 삭제 -->
          <button @click="deleteComment(comment.id)" class="btn btn-danger ml-2">삭제하기</button>

          <!-- 대댓글 -->
          <hr>
          <p>대댓글</p>
          <div v-for="children in comment.children" :key="children.id" class="re-comment card mb-2">
            <div class="card-body">
              <p class="card-text comment-content">{{ children.content }}</p>
            </div>
          </div>
          <div v-show="comment.showReComment" class="create-re-comment">
            <form @submit.prevent="createReComment(comment.id, comment)">
              <label for="reComment" class="form-label">대댓글 입력</label>
              <input type="text" id="reComment" v-model="reComment" class="form-control" placeholder="대댓글을 작성해주세요">
              <button type="submit" class="btn btn-primary ml-2">작성하기</button>
            </form>
          </div>
          <button @click="comment.showReComment = !comment.showReComment" class="btn btn-secondary ml-2">{{comment.showReComment ? '접기' : '대댓글달기'}}</button>
        </div>
      </div>
    </div>
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
.comment-container {
  border: 1px solid #ddd;
}

.like-count {
  margin-top: 5px;
  margin-bottom: 10px;
}

.modify-comment,
.create-re-comment {
  margin-top: 10px;
}

.re-comment {
  margin-top: 10px;
}

.create-comment {
  margin-top: 20px;
}

.comment-number {
  margin-left: 10px;
  color: #555;
  font-size: 12px;
}

.inputComment {
  display: flex;
  align-items: center;
}

.create-comment button {
  margin-top: 10px;
}
.btn{
  margin-right: 5px;
}
  </style>