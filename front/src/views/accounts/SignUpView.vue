<template>
  <div>
    <h1>SingUp</h1>
      <form @submit.prevent="SignUp">

        <div class="mb-3">
          <label for="name">아이디</label>
          <input type="text" id="name" v-model.trim="username">
        </div>

        <div class="mb-3">
          <label for="pw1">비밀번호</label>
          <input type="password" id="pw1" v-model.trim="password1">
        </div>

        <div class="mb-3">
          <label for="pw2">비밀번호 확인</label>
          <input type="password" id="pw2" v-model.trim="password2">
        </div>
        
        <input type="submit" value="제출하기">
      </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore} from '@/stores/counter'
import 'bootstrap/dist/css/bootstrap.min.css';

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const SignUp = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}
</script>

<style scoped>

</style>
