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
            <li class="nav-item">
              <RouterLink :to="{ name: 'RecomandView' }" class="nav-link">Recomand</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'NofityView' }" class="nav-link">NofityView ({{ notifys }})</RouterLink>
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
      <p @click="goLogin">로그인이 필요합니다.</p>
    </div>

    <RouterView />
  </div>
</template>

<script setup>
import { useCounterStore } from './stores/counter';
import { RouterView, RouterLink, useRouter } from 'vue-router'
import 'bootstrap/dist/css/bootstrap.min.css';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const router = useRouter()
const store = useCounterStore()

const notifys = ref(null)

const updateProfile = () => {
    router.push({ name: 'UpdateProfile' })
}

const goLogin = () => router.push({name: 'LogInView'})
onMounted(() => {
  if(store.isLogin){
    axios({
          method: 'GET',
          url: `${store.API_URL}/api/v1/community/isnotify/`,
          headers: {
              Authorization: `Token ${store.token}`
          }
      })
      .then((res)=>{
          console.log('notify 가져오기 성공', res);
          notifys.value = res.data.notifies
      })
      .catch((err)=>{
      console.log('notify 가져오기 실패', err)
      })
  }
});


</script>

<style scoped>

</style>
