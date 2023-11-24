<template>
    <div>
  <div class="post-item">
    <RouterLink :to="{ name: 'DetailView', params: { id: post.id } }" class="naver-link">
      <div class="post-content">
        <div class="post-header">
          <span class="post-number">#{{ post.id }}</span>
          <h4 class="post-title">{{ post.title }}</h4>
        </div>
        <p class="post-date">작성(수정)일: {{ post.updated_at.slice(0, 10) }} {{ post.updated_at.slice(11, 16) }}</p>
      </div>
    </RouterLink>
    <hr class="post-divider">
  </div>
</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

const props = defineProps({
    post: Object,
})

const post = props.post
const store = useCounterStore();
let postNum = 1

</script>

<style scoped>
.post-item {
  margin-bottom: 20px;
}

.post-content {
  background-color: #ffffff;
  padding: 15px;
  border: 1px solid #e1e1e1;
  border-radius: 8px;
  transition: background-color 0.3s ease;
}

.post-header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.post-number {
  font-size: 1.2em;
  color: #999;
  margin-right: 10px;
}

.post-title {
  color: #333;
  font-weight: bold;
  margin-bottom: 0;
}

.post-date {
  color: #666;
  margin-top: 5px;
}

.naver-link {
  text-decoration: none;
  color: inherit;
}

.post-content:hover {
  background-color: #f8f8f8;
  transform: scale(1.03);
  transition: transform 0.3s ease-in-out;
}

.post-divider {
  margin-top: 15px;
  margin-bottom: 15px;
  border: 1px solid #e1e1e1;
}
</style>
