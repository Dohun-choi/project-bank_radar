import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {


// 0. 변수
const API_URL = 'http://127.0.0.1:8000' // 주소
const token = ref(null) // 토큰
const router = useRouter()  // 라우터
const profileInfo = ref(null) // 프로필 정보
const exchanges = ref(null) // 환율 불러오기
const financeDepositsProducts = ref(null) // 예금 불러오기
const financeSavingsProducts = ref(null) // 적금 불러오기
const posts = ref(null) // 포스트 정보
const err = ref(null)
  

// 1. 로그인 유무(토큰 구하기)
const isLogin = computed(()=>{
  if (token.value === null){
      return false
  } else{
      return true
  }
  })
  
  // 2. 로그인
  const logIn = (payload) =>{
      const { username, password} = payload
      
      axios({
          method: 'post',
          url: `${API_URL}/accounts/login/`,
          data:{
          username, password
          },
      })
      .then((res)=>{
          console.log('로그인 성공', res.data)
          
          // 로그인 시 전부 로딩
          token.value = res.data.key // 토큰
          getProfile() // 8. 프로필 가져오기
          getExchange() // 3. 환율 가져오기
          getFinanceDepositsProducts() // 4. 예금 정보 가져오기
          getFinanceSavingsProducts () // 5. 적금 정보 가져오기

          router.push({name: 'MainView'})
  
      })
      .catch((err)=>{
          console.log('로그인 실패', err)
          alert('틀린 비밀번호이거나 존재하지 않는 아이디입니다.')
      })
      }
  
  // 3. 환율 가져오기
  const getExchange = ()=>{
      axios({
      method: 'GET',
      url : `${API_URL}/api/v1/exchange/`,
      headers:{
          Authorization: `Token ${token.value}`
      }
      })
      .then((res) =>{
      exchanges.value = res.data
      console.log('환율 가져오기 성공')
      })
      .catch((err)=>{
      console.log('환율 가져오기 실패', err)
      })
  }
  
  // 4. 예금 정보 가져오기
  const getFinanceDepositsProducts = () => {
      axios({
          method: 'get',
          url : `${API_URL}/api/v1/fin-product/deposits/`,
          headers:{
          Authorization: `Token ${token.value}`
          }
      })
      .then((res) =>{
          financeDepositsProducts.value = res.data
          console.log('Deposits 가져오기 성공', res.data)
      })
      .catch((err)=>{
          console.log('Deposits 가져오기 실패', err)
      })
      }
      
  // 5. 적금 정보 가져오기
      const getFinanceSavingsProducts = () => {
      axios({
          method: 'get',
          url : `${API_URL}/api/v1/fin-product/savings/`,
          headers:{
          Authorization: `Token ${token.value}`
          }
      })
      .then((res) =>{
          financeSavingsProducts.value = res.data
          console.log('Savings 가져오기 성공', res)
      })
      .catch((err)=>{
          console.log('Savings 가져오기 실패', err)
      })
      }
  
  // 7. 로그 아웃
  const logout = () => {
      token.value = null
      profileInfo.value = null
      localStorage.clear()
      alert('로그아웃 되었습니다.')
  }
  
  // 8. 프로필 받아오기
  const getProfile = ()=>{
      axios({
          method: 'GET',
          url : `${API_URL}/api/v1/recommend/profile/`,
          headers:{
          Authorization: `Token ${token.value}`
          }
      })
      .then((res) =>{
          console.log('프로필 받아오기 성공', res)
          profileInfo.value = res.data
          location.reload()
      })
      .catch((err)=>{
          console.log('프로필 받아오기 실패', err)
      })
      }
  
  // 9. 프로필 업데이트
  const updateProfile = (data)=>{
      axios({
          method: 'PUT',
          url : `${API_URL}/api/v1/recommend/profile/`,
          data: data,
          headers:{
              Authorization: `Token ${token.value}`
          }
      })
      .then((res) =>{
          console.log('프로필 수정하기 성공', res)
          profileInfo.value = res.data
          router.push({name: 'ProfileView'})
      })
      .catch((err)=>{
          console.log(data)
          console.log('프로필 수정하기 실패', err)
      })
  }


  // 10. 포스트 받기
  const getPosts = ()=>{
    axios({
      method: 'get',
      url : `${API_URL}/api/v1/community/posts/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) =>{
      console.log('포스트 받기 성공', res)
      posts.value = res.data
    })
    .catch((err)=>{
      console.log('포스트 받기 실패', err)
    })
  }


  // 11 환율 데이터 DB에 저장하기
  const updateExchange = ()=>{
    axios({
      method: 'POST',
      url : `${API_URL}/api/v1/exchange/update/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) =>{
      console.log('환율 DB에 저장 성공')
    })
    .catch((err)=>{
      console.log('환율 DB에 저장 실패', err)
    })
  }

  // 12. 금융 데이터 DB에 저장하기
  const updateFinanceProducts = () => {
    axios({
      method: 'POST',
      url : `${API_URL}/api/v1/fin-product/update/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) =>{
      console.log('금융 데이터 DB저장 성공', res)
    })
    .catch((err)=>{
      console.log('금융 데이터 DB저장 실패', err)
    })
  }

  return {posts, API_URL, getPosts, logIn,
     token, isLogin, getExchange, exchanges,
      logout,getFinanceSavingsProducts,
       getFinanceDepositsProducts, updateExchange,
        updateFinanceProducts, financeSavingsProducts,
         financeDepositsProducts, getProfile, profileInfo,
          updateProfile}
}, { persist: true })