<template>
    <div>
      <form @submit.prevent="updateProfile" class="container mt-5">
        <p> 수정사항 </p>
        <div class="mb-3">
          <label for="nickname" class="form-label">닉네임:</label>
          <input type="text" id="nickname" class="form-control" :placeholder="userInfo.nickname" v-model="nickname">
        </div>
  
        <div class="mb-3">
          <label for="birth" class="form-label">생일:</label>
          <input type="date" id="birth" class="form-control" :placeholder="userInfo.birth ? userInfo.birth.slice(0, 10) :userInfo.birth"  v-model="birth">
          <small class="form-text text-muted">0000-00-00(년/월/일) 형식으로 입력해주세요.</small>
        </div>
  
        <div class="mb-3">
          <label for="assets" class="form-label">자산(원):</label>
          <input type="text" id="assets" class="form-control" :placeholder="userInfo.assets? formatNumber(userInfo.assets) : userInfo.assets " v-model="assets">
        </div>
  
        <div class="mb-3">
          <label for="monthly_income" class="form-label">월 수입(원):</label>
          <input type="text" id="monthly_income" class="form-control" :placeholder="userInfo.monthly_income? formatNumber(userInfo.monthly_income) : userInfo.monthly_income" v-model="monthly_income">
        </div>
  
        <button type="submit" class="btn btn-primary" style="background-color: #e5007e; border-color: #e5007e;">수정하기</button>
      </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';

const store = useCounterStore();
const userInfo = store.profileInfo;

const nickname = ref(null);
const birth = ref(null);
const assets = ref(null);
const monthly_income = ref(null);

const obj = ref({ nickname, birth, assets, monthly_income });

const formatNumber = num => new Intl.NumberFormat().format(num)

const updateProfile = () => {
const data = Object.keys(obj.value).reduce((acc, cur) => {
    const refValue = obj.value[cur];
    if (refValue !== null) {
    acc[cur] = refValue;
    }
    return acc;
}, {});
store.updateProfile(data);
};
</script>

<style scoped>
/* Additional custom styles can be added here */
body {
background-color: #f8f9fa;
}
</style>