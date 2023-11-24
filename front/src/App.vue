<template>
  <div>
    <div class="title">
    
    <nav class="navbar navbar-expand-xl navbar-light">
  <div class="container">
    <!-- 네비게이션 로고 또는 브랜드 -->
    <span>
    <RouterLink :to="{ name: 'MainView' }" class="list-group-item col">
        <img src="@/assets/BankRadar_favicon.png" style="height: 80px; widows: 80px;" align="right"  alt="로고">
    </RouterLink>
</span>
    <RouterLink :to="{ name: 'MainView' }" class="list-group-item col" style="display:inline-block">
        <h1>Bank Radar
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
          <RouterLink :to="{ name: 'ExchangeMapView' }" class="nav-link" :class="{ 'active': isActive('ExchangeMapView') }">환율&지도</RouterLink>
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

        <div class="col-lg-2 my-3">
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

				<div class="parent-container">
					<img src="https://pbs.twimg.com/media/EFHNcJQUcAI_acX.jpg" alt="바다 사진">
				</div>
        </div>

        <RouterView class="col-lg-10"/>

      </div>
    </div>


    <footer class="footer mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h5>Contact Us</h5>
                    <p>Phone: -</p>
                    <p>Email: -</p>
                </div>
                <div class="col-md-4">
                    <h5>Git Hub</h5>
                    <ul class="list-inline">
                        <li class="list-inline-item"><a href="https://github.com/Dohun-choi/project-bank_radar" target="_blank">Project</a></li>
                        <li class="list-inline-item"><a href="https://github.com/MunsooKang" target="_blank">강문수</a></li>
                        <li class="list-inline-item"><a href="https://github.com/Dohun-choi" target="_blank">최도훈</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h5>Newsletter</h5>
                    <p>더 많은 금융상품과 여행지 정보에 대해 알람을 받아보세요</p>
                    <form>
                        <div class="form-group">
                            <input type="email" class="form-control" placeholder="Enter email">
                        </div>
                        <button type="submit" class="btn btn-primary">구독하기</button>
                    </form>
                </div>
            </div>
            <hr>
            <div class="row">
                <div class="col-md-6">
                    <ul class="list-inline">
                        <li class="list-inline-item"> <RouterLink to="/" @click="scrollToTop">Home</RouterLink></li>
                        <li class="list-inline-item"><a href="https://github.com/Dohun-choi/project-bank_radar"  target="_blank">Destinations</a></li>
                        <li class="list-inline-item"><a href="https://curt-poem.tistory.com/" target="_blank">Blog</a></li>
                        <li class="list-inline-item"><a href="https://github.com/Dohun-choi/project-bank_radar" target="_blank">About Us</a></li>
                    </ul>
                </div>
                <div class="col-md-6 text-right">
                    <p>&copy; 2023 Bank Radar. All rights reserved.</p>
                </div>
            </div>
        </div>
    </footer>

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

const scrollToTop = () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
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

.login-container {
  display: flex;
  flex-direction: column;
  text-align: center;
  border-radius: 10px;
  padding: 15px;
  background-color: whitesmoke; /* Magenta color */
}

a {
  text-decoration: none;
}

.parent-container {
	overflow: hidden;
	max-height: 500px;
	
	@media (max-width: 992px) {
			max-height: 00px;
	}
}



footer {
    background-color: #333;
    color: #fff;
    padding: 30px 0;
}

footer ul {
    list-style: none;
    padding: 0;
}

footer ul li {
    margin-bottom: 10px;
}

footer a {
    color: #fff;
}

footer a:hover {
    color: #aaa;
    text-decoration: none;
}
</style>
