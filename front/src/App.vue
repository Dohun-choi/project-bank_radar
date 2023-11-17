<template>
    <div>
      <div v-if="store.isLogin">
        <p>환영합니다</p>
        <button @click="store.logout">로그아웃</button>
      </div>
      <div v-else>
        로그인이 필요합니다.
      </div>
      <!-- 로컬스토리지 초기화 실험용 -->
      <button @click="clearStorage">스토리지 초기화</button>
      <nav>
        <RouterLink :to="{name: 'ArticleView'}">Posts</RouterLink>
        <br>
        <RouterLink :to="{name: 'MapView'}">Map</RouterLink>
        <br>
        <RouterLink :to="{name: 'SignUpView'}">SingUp</RouterLink>
        <br>
        <RouterLink :to="{name: 'LogInView'}">LogIn</RouterLink> 
        <br>
        <RouterLink :to="{name: 'ExchangeView'}">Exchange</RouterLink>
        <br> 
        <RouterLink :to="{name: 'FinanceView'}">Finance</RouterLink> 
      </nav>
      <RouterView />
    </div>
</template>

<script setup>
import { useCounterStore } from './stores/counter';
import { ref, computed, onMounted } from 'vue';
import { RouterView, RouterLink } from 'vue-router'

const store = useCounterStore()

const clearStorage = () => localStorage.clear()



</script>


<style scoped>

</style>
