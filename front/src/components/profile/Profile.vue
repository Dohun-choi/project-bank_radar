<template>
    <div>
      <div class="container mt-5">
        <div class="card mx-auto" style="max-width: 400px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
          <img src="@/assets/purin.jpg" class="card-img-top rounded-circle" alt="프로필 이미지" style="width: 150px; height: 150px; object-fit: cover; border: 5px solid #fff; margin-top: -75px;">
          <div class="card-body text-center">
            <h4 class="card-title h3" style="color: #e5007e;">{{ userInfo?.nickname }} 님의 프로필</h4>
            <ul class="list-group list-group-flush">
              <li class="list-group-item" style="background-color: #f8f9fa;">
                <strong>생년월일:</strong> {{ userInfo?.birth ? userInfo.birth.slice(0, 10) : null }}
              </li>
              <li class="list-group-item">
                <strong>나이:</strong> {{ userInfo?.age }}
              </li>
              <li class="list-group-item" style="background-color: #f8f9fa;">
                <strong>자산:</strong> {{ formatNumber(userInfo?.assets ? userInfo.assets : null) }}원
              </li>
              <li class="list-group-item">
                <strong>월 수입:</strong> {{ formatNumber(userInfo?.monthly_income ? userInfo.monthly_income : null) }}원
              </li>
            </ul>
  
            <button @click="updateProfile" class="btn btn-primary mt-3" style="background-color: #e5007e; border-color: #e5007e; margin-right: 10px;">프로필 수정</button>
  
            <button @click="goSubscribes" class="btn btn-primary mt-3" style="background-color: #e5007e; border-color: #e5007e;">가입 내역 확인</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';

const router = useRouter();
const store = useCounterStore();

const userInfo = store.profileInfo;

const formatNumber = num => new Intl.NumberFormat().format(num);

const updateProfile = () => router.push({ name: 'UpdateProfile' });

const goSubscribes = () => router.push({ name: 'Subscribes' });
</script>

<style scoped>
/* Additional custom styles can be added here */
body {
background-color: #f8f9fa;
}
</style>
