<template>
  <div class="signup-container p-4 rounded bg-light">
    <h1 class="mb-4 text-center">회원 가입</h1>
    <form @submit.prevent="SignUp">
      <div class="mb-3">
        <label for="name" class="form-label">아이디</label>
        <input type="text" id="name" v-model.trim="username" class="form-control" />
      </div>

      <div class="mb-3">
        <label for="pw1" class="form-label">비밀번호</label>
        <input type="password" id="pw1" v-model.trim="password1" class="form-control" />
      </div>

      <div class="mb-3">
        <label for="pw2" class="form-label">비밀번호 확인</label>
        <input type="password" id="pw2" v-model.trim="password2" class="form-control" />
      </div>

      <template v-if="err">
        <p v-for="er in err">
          {{ er[0] }}
        </p>  
      </template>
        
      
      <button type="submit" class="btn btn-magenta w-100">제출하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

const store = useCounterStore();
const API_URL = store.API_URL

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const err = ref(null)

  // 6. 회원가입
  const signUp2 = (payload) =>{
      const { username, password1, password2 } = payload
      axios({
          method: 'post',
          url: `${API_URL}/accounts/signup/`,
          data:{
          username, password1, password2
          }
      })
      .then((res)=>{
          console.log('회원가입 성공', res)
          router.push({name: 'LogInView'})
      })
      .catch((error)=>{
          console.log('회원가입 실패', error)
          err.value = error.response.data
          console.log(err)
      })
  }
  

const SignUp = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  };
  signUp2(payload);
};
</script>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
}

.btn-magenta {
  background-color: #e5007e; /* Magenta color */
  border-color: #e5007e; /* Magenta color */
  color: white;
}
</style>
