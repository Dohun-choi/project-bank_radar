<template>
<div class="container mt-4 text-left">
    <form @submit.prevent="modify" class="custom-form">
    <div class="mb-3">
        <h3 class="custom-heading">게시글 내용 수정</h3>

        <label for="title" class="form-label">제목 변경</label>
        <input type="text" id="title" v-model="title" class="form-control" maxlength="50" placeholder="제목">
        <p>{{ title.length }} / 50</p>
        <p v-if="title.length >= 50" style="color: red;">제목은 최대 50글자까지 입력가능합니다.</p>
    </div>
    <div class="mb-3">
        <label for="content" class="form-label">내용 변경</label>
        <textarea v-model.trim="content" id="content" class="form-control" placeholder="내용"></textarea>
        <p>{{ content.length }} / 1500</p>
        <p v-if="content.length >= 1500" style="color: red;">내용은 최대 1500글자까지 입력가능합니다.</p>
    </div>
    <input type="submit" value="수정하기" class="btn btn-danger">
    </form>
</div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '../../stores/counter';

const store = useCounterStore();
const router = useRouter();
const route = useRoute();
const query = route.query;
const title = ref(query.title);
const content = ref(query.content);

const modify = () => {
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
        method: 'PUT',
        url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/`,
        data: {
        title: title.value ? title.value : query.title,
        content: content.value ? content.value : query.content,
        },
        headers: {
        Authorization: `Token ${store.token}`,
        },
    })
        .then((res) => {
        console.log('성공');
        router.push({ name: 'DetailView' });
        })
        .catch((err) => {
        console.log('실패', err);
        });
    }
    };
</script>

<style scoped>
.custom-form {
max-width: 400px;
margin: 0 auto;
}

.btn-danger {
background-color: #ff69b4; /* 딸기우유 색상 */
border-color: #ff69b4; /* 딸기우유 색상 */
}

.btn-danger:hover {
background-color: #ff0080; /* 진한 딸기우유 색상 */
border-color: #ff0080; /* 진한 딸기우유 색상 */
}
.custom-heading {
color: #ff69b4; /* 딸기우유 색상 */
margin-bottom: 1.5rem; /* 아래 여백 추가 */
}
</style>
