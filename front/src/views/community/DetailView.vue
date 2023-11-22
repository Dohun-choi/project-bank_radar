<template>
  <div class="container mt-4">
    <h3 class="mb-4">게시글 상세 정보</h3>

    <div class="info card">
      <div class="card-header bg-custom text-white">
        게시글 정보
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-bordered">
            <tbody>
              <tr>
                <td class="table-header">idx</td>
                <td>{{ post.id }}</td>
              </tr>
              <tr>
                <td class="table-header">title</td>
                <td>{{ post.title }}</td>
              </tr>
              <tr>
                <td class="table-header">content</td>
                <td>{{ post.content}}</td>
              </tr>
              <tr>
                <td class="table-header">updated_at</td>
                <td>{{ post.updated_at }}</td>
              </tr>
              <tr>
                <td class="table-header">좋아요</td>
                <td>{{ post.like_count }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="d-flex justify-content-between align-items-center mt-4">
      <div>
        <button @click="deletePost" class="btn btn-danger naver-btn">DELETE</button>
        <button @click="moveModify" class="btn btn-warning naver-btn ml-2">MODIFY</button>
      </div>
      <button @click="postLike" class="btn btn-primary naver-btn">
        {{ post.is_liked ? '좋아요 취소' : '좋아요' }}
      </button>
    </div>

    <hr class="my-4">

    <!-- 댓글 컴포넌트 추가 -->
    <Comments />
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

onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
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
    });
};

// 수정 페이지로 이동
const moveModify = () => router.push({ name: 'ModifyView' });

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
</script>

<style scoped>
.info {
  border: 1px solid #ddd; /* 회색 테두리 */
  border-radius: 10px; /* 테두리 둥글게 */
}

.card-header.bg-custom {
  background-color: rgb(241, 125, 166); /* 마젠타 색상으로 변경 */
  color: white;
  font-weight: bold;
}

.table-header {
  background-color: rgb(241, 125, 166); /* 마젠타 색상으로 변경 */
  color: white;
  font-weight: bold;
}
.btn{
  margin-left: 5px;
}
</style>
