<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      
      <div>
        <label for="ID">ID</label>
      <input type="text" id="ID" v-model.trim="username">
      </div>
      
      <div>
        <label for="">PASSWORD</label>
      <input type="password" id="PASSWORD" v-model.trim="password">
      </div>

      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';

const store = useCounterStore()

const username = ref(null)
const password = ref(null)

const logIn = () => {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payload)
}
</script>

<style scoped>

</style>
