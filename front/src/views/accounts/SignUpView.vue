<template>
  <div class="signup-container p-4 rounded bg-light">
    <h1 class="mb-4 text-center">회원 가입</h1>
    <form @submit.prevent="SignUp">
      <div class="mb-3">
        <label for="name" class="form-label">아이디</label>
        <input type="text" id="name" v-model.trim="username" class="form-control" />
        <p v-for="e in errusername">{{ e }}</p>  
      </div>

      <div class="mb-3">
        <label for="pw1" class="form-label">비밀번호</label>
        <input type="password" id="pw1" v-model.trim="password1" class="form-control" />
        <p v-for="e in errpwd">{{ e }}</p>  
      </div>

      <div class="mb-3">
        <label for="pw2" class="form-label">비밀번호 확인</label>
        <input type="password" id="pw2" v-model.trim="password2" class="form-control" />
        <p v-for="e in errpwd2">{{ e }}</p>  
        <p v-if="diff">{{ '비밀번호가 일치하지 않습니다.' }}</p>
      </div>


        
      
      <button type="submit" class="btn btn-magenta w-100">제출하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import { useRouter } from 'vue-router';

const store = useCounterStore();
const API_URL = store.API_URL
const router = useRouter()

const username = ref('');
const password1 = ref('');
const password2 = ref('');
const errusername = ref([])
const errpwd = ref([])
const errpwd2 = ref([])
const diff = ref(null)

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
          errusername.value = error.response.data.username
          errpwd.value = error.response.data.password1
          errpwd2.value = error.response.data.password2
          diff.value = error.response.data.non_field_errors
      })
  }
  

const SignUp = () => {
    if (containsNonAlphaNumeric(username.value)) {
        errusername.value = ['아이디는 영문 또는 숫자의 조합으로만 가능합니다.']
        return
    } else if (username.value.length < 5) {
        errusername.value = ['아이디는 최소 5글자 이상이어야합니다.']
        return
    }
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  };
  signUp2(payload);
};

const containsNonAlphaNumeric = (username) => {
  for (let i = 0; i < username.length; i++) {
    const character = username[i];
    if (!/^[a-zA-Z0-9]$/.test(character)) {
      return true;
    }
  }
  return false;
}
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
