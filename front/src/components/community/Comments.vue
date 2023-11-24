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

const isLogin = useCounterStore().isLogin

const showModify = ref(false);
const showReComment = ref(false)

const createComment = () => {
    if (content.value.length==0) {
        return alert('내용을 입력해 주세요')
    } else if (content.value.length>200) {
        return alert('내용은 200자를 넘어갈 수 없습니다.')
    }
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
const confirmed = confirm('정말 댓글을 삭제하시겠습니까?');
if (confirmed) {
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
})}
}

// 댓글 수정
const commentModify = () => {
    if (newContent.value.length==0) {
        return alert('내용을 입력해 주세요')
    } else if (newContent.value.length>200) {
        return alert('내용은 200자를 넘어갈 수 없습니다.')
    }
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
  comment.value.children = updatedComments;
};

const setRecomment = () => {
  showReComment.value = !showReComment.value
  showModify.value = false
}

const setModify = () => {
  showReComment.value = false
  showModify.value = !showModify.value
}

</script>

<template>
  <div class="card mx-1">
    <div class="comment-container" v-if="comment.content">
      <div style="display: flex; justify-content: space-between; align-items: center;">

        <div class="nickname-and-likes">
          <p style="font-size: 20px; display: inline-block;"> {{ comment.profile.nickname }}</p>
          <p>{{ comment.updated_at.slice(0, 10) }} {{ comment.updated_at.slice(11, 16) }}</p>
          <p style="font-size: 13px; display: inline-block;" v-if="parentname">{{ parentname }}님에게 보내는 답글</p>
        </div>
        <button @click="commentLike"  v-if="isLogin" :class="{
        'btn': true,
        'btn-info': comment.is_liked,
        'btn-outline-info': !comment.is_liked
          }"
          style="color: red;">💕{{ comment.like_count }}
        </button>
      </div>

      <p>{{ comment.content }}</p>
      
      <div class="button-container">
        <div>
    </div>



      <template v-if="store.profileInfo?.id === comment.user">

        <button @click="deleteComment" class="btn btn-danger ml-2">삭제</button>

        <form v-if="isLogin && showModify" @submit.prevent="commentModify" class="modify-comment">
          <div class="d-flex align-items-center">
            <input type="text" id="newContent" v-model="newContent" class="form-control" placeholder="수정할 내용을 작성해주세요"  maxlength="200">
            <p v-if="newContent.length >= 200" style="color: red;">최대 200글자까지 입력가능합니다.</p>
            <button type="submit" class="btn btn-primary ml-2" style="white-space: nowrap; width: auto;">수정</button>
          </div>
          </form>
        <button @click="setModify" class="btn btn-warning ml-2">{{showModify? '접기' : '수정'}}</button>

      </template>

        <form v-if="isLogin && showReComment" @submit.prevent="createComment" class="create-re-comment form-inline">
          <div class="d-flex align-items-center">
            <input type="text" id="reComment" v-model="content" class="form-control" placeholder="대댓글을 작성해주세요" maxlength="200">
            <p v-if="content.length >= 200" style="color: red;">최대 200글자까지 입력가능합니다.</p>
            <button type="submit" class="btn btn-primary ml-2" style="white-space: nowrap; width: auto;">작성</button>
          </div>
        </form>
        <button  v-if="isLogin" @click="setRecomment" class="btn btn-success ml-2">{{showReComment ? '접기' : '답글'}}</button>
      
      </div>
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

.btn-danger:hover {
  background-color: red;
  border: red 1px;
}

.btn-danger {
  background-color: rgb(220,53,69);
  border: rgb(220,53,69) 1px;
}

.btn-info {
  background-color: rgb(241, 125, 166);
  border: rgb(241, 125, 166) solid 1px;
}
.btn-outline-info {
    border: rgb(241, 125, 166) solid 1px;
}

.btn-outline-info:hover,
.btn-outline-info:active,
.btn-info:hover,
.btn-info:active {
    border: rgb(255, 182, 208) solid 1px;
    background-color: rgb(255, 182, 208);
}

.button-container {
  display: flex;
  justify-content: flex-end;
}

.nickname-and-likes {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
  </style>