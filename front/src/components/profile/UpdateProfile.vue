<template>
    <div>
        <form @submit.prevent="updateProfile">
            <div>
                <label for="nickname">닉네임 : </label>
                <input type="text" id="nickname" :placeholder="userInfo.nickname" v-model="nickname">
            </div>

            <div>
                <label for="birth">생일 : </label>
                <input type="text" id="birth" :placeholder="userInfo.birth" v-model="birth">
            </div>

            <div>
                <label for="assets">자산 : </label>
                <input type="text" id="assets" :placeholder="userInfo.assets" v-model="assets">
            </div>

            <div>
                <label for="monthly_income">월 수입 : </label>
                <input type="text" id="monthly_income" :placeholder="userInfo.monthly_income" v-model="monthly_income">
            </div>
            <input type="submit" value="수정하기">
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

const userInfo = store.profileInfo

const nickname = ref(null)
const birth = ref(null)
const assets = ref(null)
const monthly_income = ref(null)

const obj = ref({
    nickname, birth, assets, monthly_income
    })


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

</style>