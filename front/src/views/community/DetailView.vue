<template>
    <div>
    <div class="container mt-4">

    <div class="info card">

      <div class="card-header bg-custom text-white">
        <p>{{ post.profile ? post.profile.nickname : '탈퇴한 유저' }}님의 글</p>
        <h3>{{post.title}}</h3>
        <p>추천({{post.like_count }})</p>
      </div>

      <div class="card-body">
        {{ post.content }}
      </div>
      
      <div class="d-flex justify-content-between align-items-center mt-4">
        <template v-if="store.profileInfo?.id === post.user">
      <div>
        <button @click="deletePost" class="btn btn-danger naver-btn">삭제</button>
        <button @click="moveModify" class="btn btn-warning naver-btn ml-2">수정</button>
      </div>

    </template>
      <button v-if="isLogin" @click="postLike" :class="{
      'btn': true,
      'btn-info': post.is_liked,
      'btn-outline-info': !post.is_liked
    }">💕
      </button>

      </div>

    </div>

    <hr class="my-4">
    <div v-if="isLogin" class="create-comment">
      <form @submit.prevent="createComment">
        <label for="comment" class="form-label"><strong>댓글 {{ post.comment_count }}개</strong></label>
        <div>
          <input type="text" id="comment" v-model="commentcontent" class="form-control" placeholder="댓글을 입력해주세요." maxlength="200">
          <p v-if="commentcontent.length >= 200" style="color: red;">최대 200글자까지 입력가능합니다.</p>
          {{ commentcontent.length }} / 200
          <button type="submit" class="btn btn-primary ml-2" style="float: right; display: block;">댓글달기</button>
        </div>
      </form>
    </div>
    <hr>

    <!-- 댓글 컴포넌트 추가 -->
        <Comments v-for="comment in post.comment_set"
            :comment="comment"
            :post_pk="post.id"
            :parent="null"
            :key="comment.id"
            :parentname = "null"
            @delete-comment="removeComment(comment)"/>
  </div>
</div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';
import Comments from '@/components/community/Comments.vue';

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const post = ref([]);
const commentcontent = ref('')
const isLogin = store.isLogin


onMounted(() => {
    const config = {
        method: 'GET',
        url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/`,
    }

    if (store.token !== null) {
        config.headers = {
        Authorization: `Token ${store.token}`
        }
    }
  axios(config)
    .then((res) => {
      console.log('게시글 세부 정보 가져오기 성공', res.data);
      post.value = res.data;
    })
    .catch((err) => {
      console.log('게시글 세부 정보 가져오기 실패', err);
    });
});

// 게시글 삭제하기
const deletePost = () => {
    const confirmed = confirm('정말 게시글을 삭제하시겠습니까?');
    if (confirmed) {
  axios({
    method: 'DELETE',
    url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log('게시글 삭제 성공');
      router.push({ name: 'ArticleView' });
    })
    .catch((err) => {
      console.log('게시글 삭제 실패', err);
    })
}
};

// 수정 페이지로 이동
const moveModify = () => {
    router.push({
        name: 'ModifyView',
        query: {
        title: post.value.title,
        content: post.value.content
        }
})}

// 게시글 좋아요
const postLike = () => {
  axios({
    method: 'POST',
    url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/likes/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log('성공');
      post.value.is_liked = res.data.isLiked;
      post.value.like_count = res.data.likeCount;
    })
    .catch((err) => {
      console.log('실패', err);
    });
};


const createComment = () => {
    if (commentcontent.value.length==0) {
        return alert('내용을 입력해 주세요')
    } else if (commentcontent.value.length>200) {
        return alert('내용은 200자를 넘어갈 수 없습니다.')
    }
  const config = {
      method: 'POST',
      url: `${store.API_URL}/api/v1/community/posts/${post.value.id}/comments/`,
      data: {
        content: commentcontent.value,
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
  }

  axios(config)
  .then((res)=>{
    console.log('댓글 작성 성공', res.data)
    post.value.comment_set.push(res.data)
    commentcontent.value = ''
  })
  .catch((err)=>{
    console.log('댓글 작성 실패', err)
  }) 
}



// 댓글 삭제시 컴포넌트 해제
const removeComment = (commentToRemove) => {
  const index = post.value.comment_set.filter((comment) => comment.id !== commentToRemove.id);
  if (index !== -1) {
    post.value.comment_set.splice(index, 1);
  }
};
</script>

<style scoped>
.info {
  border-radius: 10px; /* 테두리 둥글게 */
  width: 100%;
  height: 15%;
  border: 1px solid rgb(241, 125, 166);
}

.card-header.bg-custom {
  display: flex;
  justify-content: space-between;
  background-color: rgb(241, 125, 166); 
  color: white;
  font-weight: bold;
}

.table-header {
  background-color: rgb(241, 125, 166); 
  color: white;
  font-weight: bold;
}

.btn{
  margin: 5px;
}

.btn-danger {
  background-color: rgb(220,53,69);
  border: rgb(220,53,69) 1px;
}

.btn-danger:hover {
  background-color: red;
  border: red 1px;
}

.btn-info {
  background-color: rgb(241, 125, 166);
  border: rgb(241, 125, 166) solid 1px;
}
.btn-outline-info {
    border: rgb(241, 125, 166) solid 1px;
}

.btn-outline-info:hover {
    border: rgb(255, 182, 208) solid 1px;
    background-color: rgb(255, 182, 208);
}
</style>
