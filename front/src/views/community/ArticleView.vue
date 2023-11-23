<template>
  <div>
    <div  class="article-page-container">
    <h1 class="text-center mb-4">자유 게시판</h1>
    <div class="contain">
      <Search class="m-1 mb-3" @search="handleSearch"/>
      <div>
        <RouterLink :to="{name: 'CreateView'}" class="btn btn-magenta mb-3 m-1">글쓰기</RouterLink>
        <button @click="popular" class="btn btn-magenta mb-3 m-1">{{ seePopular ? '인기글':'전체글' }}</button>
      </div>
    </div>

    <div style="margin-left: auto; text-align: right;" class="m-1 mx-2">
      <select v-model="itemsPerPage">
        <option :value="2">2개씩 보기</option>
        <option :value="5">5개씩 보기</option>
        <option :value="10">10개씩 보기</option>
        <option :value="25">25개씩 보기</option>
      </select>
    </div>
    
    <template v-if="paginatedPosts.length > 0">
        <!-- Display paginated posts using ArticleListItem component -->
        <ArticleListItem
          v-for="post in paginatedPosts"
          :key="post.id"
          :post="post"
        />
        
        <!-- Pagination controls -->
        <div class="center">
          <div class="fit-content">
          <button class="btn btn-outline-secondary m-1"
            @click="changePage(1)"
            v-if="currentPage !== 1"
            >
            First
            </button>
            <template v-for="pageNumber in displayedPages" :key="pageNumber">
              <button class="btn button-outline-secondary m-1"
                      @click="changePage(pageNumber)"
                      :class="{ 'btn-secondary': pageNumber === currentPage }"
                      :style="{ color: pageNumber === currentPage ? 'white' : '', display: 'inline-block', maxWidth: 'fit-content' }">
                {{ pageNumber }}
              </button>
            </template>

          <button class="btn btn-outline-secondary m-1"
            @click="changePage(totalPages)"
            v-if="currentPage !== totalPages"
            >
            Last
          </button>
        </div>
      </div>
      </template>
      <template v-else>
        <p>Loading...</p>
      </template>

  </div>
</div>
</template>

<script setup>
import ArticleListItem from '@/components/articles/ArticleListItem.vue'
import Search from '@/components/community/Search.vue'
import { onMounted, ref, computed, watch } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import axios from 'axios';

const posts = ref(null)
const store = useCounterStore()
const API_URL = store.API_URL
const token = store.token

const currentPage = ref(1);
const itemsPerPage = ref(5)

watch(itemsPerPage, () => {
  currentPage.value = 1;
});


const url = computed(() => {
  if(seePopular.value) {
    return `${API_URL}/api/v1/community/posts/popular`
  } else {
    return `${API_URL}/api/v1/community/posts/`
  }
})
const seePopular = ref(true)

onMounted(async () => {
  await fetchPosts();
});

const fetchPosts = async () => {
  try {
    const response = await axios({
      method: 'get',
      url: `${API_URL}/api/v1/community/posts/`,
      headers: {
        Authorization: `Token ${token}`
      }
    });
    
    if (response.status === 200) {
      posts.value = response.data;
    } else {
      console.error('Failed to fetch posts:', response.statusText);
    }
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
};


const popular = () => {
    axios({
      method: 'get',
      url : url.value,
      headers:{
        Authorization: `Token ${token}`
      }
    })
    .then((res) =>{
      console.log('성공', res)
      posts.value = res.data
      seePopular.value = !seePopular.value
    })
    .catch((err)=>{
      console.log('실패', err)
    })
}

const paginatedPosts = computed(() => {
  if (!posts.value) return [];
  const startIndex = (currentPage.value - 1) * itemsPerPage.value;
  const endIndex = startIndex + itemsPerPage.value;
  return posts.value.slice(startIndex, endIndex);
});

const totalPages = computed(() => {
  if (!posts.value) return 0;
  return Math.ceil(posts.value.length / itemsPerPage.value);
});

const changePage = (pageNumber) => {
  currentPage.value = pageNumber;
};

const displayedPages = computed(() => {
  const maxPages = Math.min(totalPages.value, 5); // Maximum displayed page numbers
  const sideCount = Math.floor(maxPages / 2); // Number of pages on each side of the current page
  let startPage = Math.max(currentPage.value - sideCount, 1);
  let endPage = startPage + maxPages - 1;

  if (endPage > totalPages.value) {
    endPage = totalPages.value;
    startPage = Math.max(totalPages.value - maxPages + 1, 1);
  }

  return Array.from({ length: endPage - startPage + 1 }, (_, i) => startPage + i);
});


const handleSearch = (data) => {
  console.log('emit 받음',data)
  posts.value = data
}

</script>

<style scoped>
.article-page-container {
  max-width: 100%;
  margin: 0 auto;
}

.btn-magenta {
  background-color: rgb(241, 125, 166);
  border-color: rgb(241, 125, 166);
  color: white;
}
.contain{
  display: flex;
  justify-content: space-between;
}

.center {
  display: flex;
  justify-content: space-around;
}

.center .fit-conent {
  max-width: fit-content;
}
</style>