<template>
    <div>
      <div v-if="store.isLogin">
        <p>{{store.profileInfo.nickname}} 님 환영합니다</p>
        <div v-if="store.profileInfo.nickname === `unknown${store.profileInfo.id}`">
          <p>회원정보를 입력하시겠어요?</p>
          <button @click="updateProfile"> 회원정보 수정하기</button>
        </div>
        <button @click="store.logout">로그아웃</button>
      </div>
      <div v-else>
        로그인이 필요합니다.
      </div>
    
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
        <br> 
        <RouterLink :to="{name: 'ProfileView'}">Profile</RouterLink> 
      </nav>
      <RouterView />
    </div>
</template>

<script setup>
import { useCounterStore } from './stores/counter';
import { RouterView, RouterLink, useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()

const updateProfile = () => {
    router.push({name: 'UpdateProfile'})
}



</script>


<style scoped>

</style>
