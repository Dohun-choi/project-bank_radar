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
    <div class="container, babo" >
      <div class="row">
        <div class=" col-2">
          <ul class="list-group">
            <RouterLink :to="{ name: 'MainView' }" class="list-group-item" :class="{ 'active': isActive('MainView') }">메인 페이지</RouterLink>
            <RouterLink :to="{ name: 'ArticleView' }" class="list-group-item" :class="{ 'active': isActive('ArticleView') }">게시글</RouterLink>
            <RouterLink :to="{ name: 'FinanceDepositsView' }" class="list-group-item" :class="{ 'active': isActive('FinanceDepositsView') }">예금</RouterLink>
            <RouterLink :to="{ name: 'FinanceSavingsView' }" class="list-group-item" :class="{ 'active': isActive('FinanceSavingsView') }">적금</RouterLink>
            <RouterLink :to="{ name: 'ExchangeView' }" class="list-group-item" :class="{ 'active': isActive('ExchangeView') }">환율</RouterLink>
            <RouterLink :to="{ name: 'RecommendItemView' }" class="list-group-item" :class="{ 'active': isActive('RecommendItemView') }">적금 상품 추천</RouterLink>
            <RouterLink :to="{ name: 'RecommendTravelView' }" class="list-group-item" :class="{ 'active': isActive('RecommendTravelView') }">여행지 추천</RouterLink>
          </ul>
        </div>
        <RouterView class="col-8"/>
        <div class="col-2">
          <div v-if="!CounterStore.isLogin" class="login-container" >
            <LogInView/>
              <br>
              <p>아직 계정이 없으시다면?</p>
              <button class="btn btn-primary" style="background-color: #e5007e; border-color: #e5007e;">
                <RouterLink :to="{ name: 'SignUpView' }" style="color: white;" >회원가입</RouterLink>
              </button>
          </div>
          <SimpleProfile v-if="CounterStore.isLogin"/>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import 'bootstrap/dist/css/bootstrap.min.css';
import { RouterView, RouterLink, useRoute } from 'vue-router'
import LogInView from '@/views/accounts/LoginView.vue'
import { useCounterStore } from '@/stores/counter'
import SimpleProfile from './components/profile/SimpleProfile.vue';

const CounterStore = useCounterStore()
const route = useRoute()

const isActive = (routeName) => {
  return route.name === routeName
}
</script>

<style scoped>
.title {
  margin-bottom: 15px;
  background-color: aliceblue;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.list-group-item.active {
  background-color: rgb(83, 121, 228) /* 활성화된 아이템 배경색 */
}

.list-group-item:hover {
  background-color: #979191; /* 마우스 오버 시 배경색 변경 */
}

.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border-radius: 10px;
  padding: 15px;
  background-color: whitesmoke; /* Magenta color */
}
</style>
