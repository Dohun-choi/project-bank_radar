<template>
  <div>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand">Nav Bar</a>

        <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button> -->

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link">Home</a>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'ArticleView' }" class="nav-link">Posts</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'MapView' }" class="nav-link">Map</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'SignUpView' }" class="nav-link">SignUp</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'LogInView' }" class="nav-link">LogIn</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'ExchangeView' }" class="nav-link">Exchange</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'FinanceView' }" class="nav-link">Finance</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'ProfileView' }" class="nav-link">Profile</RouterLink>
            </li>
          </ul>
        </div>

      </div>
    </nav>

    <div v-if="store.isLogin">
      <p>{{ store.profileInfo.nickname }} 님 환영합니다</p>
      <div v-if="store.profileInfo.nickname === `unknown${store.profileInfo.id}`">
        <p>회원정보를 입력하시겠어요?</p>
        <button @click="updateProfile"> 회원정보 수정하기</button>
      </div>
      <button @click="store.logout">로그아웃</button>
    </div>
    <div v-else>
      로그인이 필요합니다.
    </div>

    <RouterView />
  </div>
</template>

<script setup>
import { useCounterStore } from './stores/counter';
import { RouterView, RouterLink, useRouter } from 'vue-router'
import 'bootstrap/dist/css/bootstrap.min.css';

const router = useRouter()
const store = useCounterStore()

const updateProfile = () => {
    router.push({ name: 'UpdateProfile' })
}

</script>

<style scoped>

</style>
