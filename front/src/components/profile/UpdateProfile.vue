<template>
    <div>
      <form @submit.prevent="updateProfile" class="container mt-5">
        <p> 수정사항 </p>
        <div class="mb-3">
          <label for="nickname" class="form-label">닉네임:</label>
          <input type="text" id="nickname" class="form-control" :placeholder="userInfo.nickname" v-model="nickname" maxlength="15">
          <small v-if="nickname.length === 15" class="form-text text-muted">닉네임은 최대 15자까지 설정가능합니다.</small>
        </div>
  
        <div class="mb-3">
          <label for="birth" class="form-label">생일:</label>
          <input type="date" id="birth" class="form-control" :placeholder="userInfo.birth ? userInfo.birth.slice(0, 10) :userInfo.birth"  v-model="birth" :max="today">
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
const today = new Date().toISOString().split('T')[0];

const nickname = ref('');
const birth = ref('');
const assets = ref('');
const monthly_income = ref('');

const obj = ref({ nickname, birth, assets, monthly_income });

const formatNumber = num => new Intl.NumberFormat().format(num)

const updateProfile = () => {
    if (nickname.value.length > 15) {
        alert('닉네임은 15자를 넘을 수 없습니다.')
    }
    assets.value = assets.value.replace(/,/g, '')
    monthly_income.value = monthly_income.value.replace(/,/g, '')

    if (isNaN(assets.value)) {
        alert('자산을 숫자 형식으로 입력해 주세요')
    }

    if (isNaN(monthly_income.value)) {
        alert('월 수입을 숫자 형식으로 입력해 주세요')
    }
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