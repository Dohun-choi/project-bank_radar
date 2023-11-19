<template>
    <button @click="updateProfile">프로필 수정하기</button>
    <div>
        <h1>Profile ㅎㅇ</h1>
        <p>user_id : {{ userInfo.id }} </p>
        <p>user_age : {{userInfo.age}}</p>
        <p>user_age_gruop : {{userInfo.age_group}}</p>
        <p>user_assets :{{userInfo.assets}}</p>
        <p>user_assets_gruop : {{userInfo.assets_group}}</p>
        <p>user_birth : {{userInfo.birth}}</p>
        <p>user_monthly_income : {{userInfo.monthly_income}}</p>
        <p>user_monthly_income_group :{{userInfo.monthly_income_group}}</p>
        <p>user_nickname : {{userInfo.nickname}}</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useCounterStore } from '../../stores/counter';

const router = useRouter()
const store = useCounterStore()
const updateProfile = () => {
    router.push({name: 'UpdateProfile'})
}

const userInfo = store.profileInfo
</script>

<style  scoped>

</style>