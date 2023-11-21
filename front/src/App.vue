<template>
  <div>
    <div class="title">
    <div class="container">
      <RouterLink :to="{ name: 'MainView' }" class="list-group-item col" style="display:inline-block">
        <img src="@/assets/BankRadar_favicon.png" style="height: 150px;"  alt="로고">
      </RouterLink>
      <RouterLink :to="{ name: 'MainView' }" class="list-group-item col" style="display:inline-block">
        <h1 style="color: lab(46.05 58.95 17.38);">TraVing
          <small class="text-body-secondary">여행을 위한 저축</small>
        </h1>
      </RouterLink>
    </div>
    </div>
    <div class="container">
      <div class="row">
        <ul class="list-group col-2">
          <RouterLink :to="{ name: 'ArticleView' }" class="list-group-item">게시글</RouterLink>
          <RouterLink :to="{ name: 'FinanceView' }" class="list-group-item">예금</RouterLink>
          <RouterLink :to="{ name: 'FinanceView' }" class="list-group-item">적금</RouterLink>
          <RouterLink :to="{ name: 'ExchangeView' }" class="list-group-item">환율</RouterLink>
          <RouterLink :to="{ name: 'RecomandView' }" class="list-group-item">적금 상품 추천</RouterLink>
          <RouterLink :to="{ name: 'RecomandView' }" class="list-group-item">여행지 추천</RouterLink>
        </ul>
        <RouterView class="col-8"/>
        <div  class="col-2">
          <template v-if="!CounterStore.isLogin">
            <LogInView/>
            <button>
              <RouterLink :to="{ name: 'SignUpView' }" class="list-group-item">회원가입</RouterLink>
            </button>
          </template>
          <SimpleProfile v-if="CounterStore.isLogin"/>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import 'bootstrap/dist/css/bootstrap.min.css';
import { RouterView, RouterLink } from 'vue-router'
import LogInView from '@/views/accounts/LoginView.vue'
import { useCounterStore } from '@/stores/counter'
import SimpleProfile from './components/profile/SimpleProfile.vue';

const CounterStore = useCounterStore()

</script>

<style scoped>
.title {
  margin-bottom: 15px;
}
</style>
