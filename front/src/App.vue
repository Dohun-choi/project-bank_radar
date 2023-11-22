<template>
  <div>
    <div class="title">
    
    <div class="container">
    </div>
    <nav class="navbar navbar-expand-xl navbar-light">
  <div class="container-fluid">
    <!-- 네비게이션 로고 또는 브랜드 -->
    <RouterLink :to="{ name: 'MainView' }" class="list-group-item col" style="display:inline-block">
        <img src="@/assets/BankRadar_favicon.png" style="height: 80px; widows: 80px;"  alt="로고">
    </RouterLink>

    <RouterLink :to="{ name: 'MainView' }" class="list-group-item col" style="display:inline-block">
        <h1 style="color: lab(46.05 58.95 17.38);">Bank Radar
          <small class="text-body-secondary" style="display: block;">여행을 위한 저축</small>
        </h1>
      </RouterLink>
    <!-- 햄버거 메뉴 아이콘 - 모바일에서 보일 때 -->
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <!-- 실제 네비게이션 목록 -->
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <RouterLink :to="{ name: 'MainView' }" class="nav-link" :class="{ 'active': isActive('MainView') }">메인 페이지</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'ArticleView' }" class="nav-link" :class="{ 'active': isActive('ArticleView') }">게시글</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'FinanceDepositsView' }" class="nav-link" :class="{ 'active': isActive('FinanceDepositsView') }">예금</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'FinanceSavingsView' }" class="nav-link" :class="{ 'active': isActive('FinanceSavingsView') }">적금</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'ExchangeView' }" class="nav-link" :class="{ 'active': isActive('ExchangeView') }">환율</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'RecommendItemView' }" class="nav-link" :class="{ 'active': isActive('RecommendItemView') }">적금 상품 추천</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'RecommendTravelView' }" class="nav-link" :class="{ 'active': isActive('RecommendTravelView') }">여행지 추천</RouterLink>
        </li>
      </ul>
    </div>
  </div>
</nav>

    </div>
    <div class="container" >
      <div class="row">

        <div class="col-lg-2  mt-3">
          <div v-if="!CounterStore.isLogin" class="login-container" >
            <LogInView/>
              <br>
              <p>아직 계정이 없으시다면?</p>
              <button class="btn btn-primary" style="background-color: #e5007e; border-color: #e5007e;">
                <RouterLink :to="{ name: 'SignUpView' }" style="color: white;" >회원가입</RouterLink>
              </button>
          </div>
          <div v-if="CounterStore.isLogin">
            <SimpleProfile />
        </div>

        <!-- <div class="mt-3">
          <ul class="list-group">
            <RouterLink :to="{ name: 'MainView' }" class="list-group-item" :class="{ 'active': isActive('MainView') }">메인 페이지</RouterLink>
            <RouterLink :to="{ name: 'ArticleView' }" class="list-group-item" :class="{ 'active': isActive('ArticleView') }">게시글</RouterLink>
            <RouterLink :to="{ name: 'FinanceDepositsView' }" class="list-group-item" :class="{ 'active': isActive('FinanceDepositsView') }">예금</RouterLink>
            <RouterLink :to="{ name: 'FinanceSavingsView' }" class="list-group-item" :class="{ 'active': isActive('FinanceSavingsView') }">적금</RouterLink>
            <RouterLink :to="{ name: 'ExchangeView' }" class="list-group-item" :class="{ 'active': isActive('ExchangeView') }">환율</RouterLink>
            <RouterLink :to="{ name: 'RecommendItemView' }" class="list-group-item" :class="{ 'active': isActive('RecommendItemView') }">적금 상품 추천</RouterLink>
            <RouterLink :to="{ name: 'RecommendTravelView' }" class="list-group-item" :class="{ 'active': isActive('RecommendTravelView') }">여행지 추천</RouterLink>
          </ul>
        </div> -->

    </div>

        <RouterView class="col-lg-10"/>

        

      </div>
    </div>

  </div>
</template>

<script setup>
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { RouterView, RouterLink, useRoute } from 'vue-router'
import LogInView from '@/views/accounts/LoginView.vue'
import { useCounterStore } from '@/stores/counter'
import SimpleProfile from '@/components/profile/SimpleProfile.vue';

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
