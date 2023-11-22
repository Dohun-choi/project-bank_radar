<template>
  <div>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1 class="text-center mb-4" style="color: #e5007e;">Login</h1>
        <form @submit.prevent="logIn">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" class="form-control" id="username" v-model.trim="username" style="width: 100%;">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" v-model.trim="password" style="width: 100%;">
          </div>
          <button type="submit" class="btn btn-primary" style="background-color: #e5007e; border-color: #e5007e;">Log In</button>
        </form>
      </div>
    </div>
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
/* Additional custom styles can be added here */
body {
background-color: #f8f9fa;
}
</style>
