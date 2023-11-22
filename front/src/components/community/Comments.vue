<script setup>
import Comments from '@/components/community/Comments.vue'
import axios from 'axios';
import { ref, getCurrentInstance  } from 'vue'
import { useCounterStore } from '../../stores/counter';

const currentInstance = getCurrentInstance();

const store = useCounterStore()

const props = defineProps({
  comment: Object,
  post_pk: Number,
  parent: Number,
  parentname : String
})

const { post_pk, parent, parentname } = props
const comment = ref(props.comment)
const content = ref('')
const newContent = ref('')

const showModify = ref(false);
const showReComment = ref(false)

const createComment = () => {
  const config = {
      method: 'POST',
      url: `${store.API_URL}/api/v1/community/posts/${post_pk}/comments/`,
      data: {
        content: content.value,
        parent: comment.value.id
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
  }

  axios(config)
  .then((res)=>{
    console.log('댓글 작성 성공', res.data)
    comment.value.children.push(res.data)
    content.value = ''
  })
  .catch((err)=>{
    console.log('댓글 작성 실패', err)
  }) 
}


// 댓글 삭제
const deleteComment = () => {
  axios({
    method: 'DELETE',
    url: `${store.API_URL}/api/v1/community/comments/detail/${comment.value.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
})
.then((res)=>{
  console.log('성공', res.data)
  currentInstance.emit('delete-comment');
})
.catch((err)=>{
  console.log('실패', err)
}) 
}

// 댓글 수정
const commentModify = () => {
  axios({
        method: 'PUT',
        url: `${store.API_URL}/api/v1/community/comments/detail/${comment.value.id}/`,
        data : {
            content: newContent.value
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
.then((res)=>{
    console.log('성공', res.data)
    comment.value = res.data
    newContent.value = ''
})
.catch((err)=>{
    console.log('실패', err)
}) 
}

// 댓글 좋아요
const commentLike = () => {
  axios({
        method: 'POST',
        url: `${store.API_URL}/api/v1/community/comments/${comment.value.id}/likes/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
.then((res)=>{
      console.log('댓글 좋아요 성공');
      comment.value.is_liked = ref(res.data.isLiked)
      comment.value.like_count = ref(res.data.likeCount)
})
.catch((err)=>{
    console.log('실패', err)
}) 
}

// 댓글 삭제시 컴포넌트 해제
const removeComment = (commentToRemove) => {
  console.log(commentToRemove)
  const updatedComments = comment.value.children.filter(comment => comment.id !== commentToRemove.id);
  comment.value = updatedComments;
};


</script>

<template>
  <div class="card">
    <div class="comment-container" v-if="comment.content">
      <p style="font-size: 20px; display: inline-block;"> {{ comment.profile.nickname }}</p>
      <p style="font-size: 13px; display: inline-block;" v-if="parentname">{{ parentname }}님에게 보내는 답글</p>

      <p>{{ comment.content }}</p>

      <p class="card-text like-count">좋아요 : {{ comment.like_count }} 개</p>
      <button @click="commentLike" class="btn btn-primary">
        {{ comment.is_liked ? '좋아요 취소' : '좋아요' }}
      </button>

      <template v-if="store.profileInfo.id === comment.user">
        <form v-show="showModify && comment.user" @submit.prevent="commentModify" class="modify-comment">
            <label for="newContent" class="form-label">댓글 수정</label>
            <input type="text" id="newContent" v-model="newContent" class="form-control">
            <button type="submit" class="btn btn-warning ml-2">수정하기</button>
        </form>
        <button @click="showModify = !showModify" class="btn btn-secondary ml-2">{{showModify? '접기' : '수정하기'}}</button>
        
        <button @click="deleteComment" class="btn btn-danger ml-2">댓글 삭제</button>
      </template>
      <form @submit.prevent="createComment" v-show="showReComment" class="create-re-comment">
        <label for="reComment" class="form-label">대댓글 입력</label>
        <input type="text" id="reComment" v-model="content" class="form-control" placeholder="대댓글을 작성해주세요">
        <button type="submit" class="btn btn-primary ml-2">작성하기</button>
      </form>
      <button @click="showReComment = !showReComment" class="btn btn-secondary ml-2">{{showReComment ? '접기' : '대댓글달기'}}</button>

        <Comments
          v-for="child in comment.children"
          :key="child.id" :comment="child"
          :post_pk="post_pk"
          :parent="comment.id"
          :parentname = "comment.profile.nickname"
          @delete-comment="removeComment(child)"
          />
    </div>
  </div>
</template>

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