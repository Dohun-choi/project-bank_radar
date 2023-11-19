import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const posts = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  
  const nickname = ref(null)
  const router = useRouter()
  // 로그인 유무
  const isLogin = computed(()=>{
    if (token.value === null){
      return false
    } else{
      return true
    }
  })
  // 환율 데이터
  const exchanges = ref(null)

  // 금융 데이터
  const financeDepositsProducts = ref(null)
  const financeSavingsProducts = ref(null)


  // 프로필 정보
  const profileInfo = ref(null)
  const profileLikes = ref(null)
  // actions


  // 프로필 좋아요 데이터 가져오기
  const getProfileLikes = ()=>{
    axios({
      method: 'GET',
      url : `${API_URL}/accounts/user/info/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) =>{
      console.log('프로필 좋아요 데이터 가져오기 성공', res.data)
      profileLikes.value = res.data
    })
    .catch((err)=>{
      console.log('프로필 좋아요 데이터 가져오기 실패', err)
    })
  }

 // 프로필 받아오기
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
    })
    .catch((err)=>{
      console.log('프로필 받아오기 실패', err)
    })
  }
  // 프로필 업데이트
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

  // 포스트 받기
  const getPosts = ()=>{
    axios({
      method: 'get',
      url : `${API_URL}/api/v1/community/posts/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) =>{
      console.log('성공', res)
      posts.value = res.data
    })
    .catch((err)=>{
      console.log('실패', err)
    })
  }

  // 회원가입
  const signUp = (payload) =>{
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data:{
        username, password1, password2
      }
    })
    .then((res)=>{
      console.log(' 회원가입 성공')
      router.push({name: 'LogInView'})
    })
    .catch((err)=>{
      console.log('회원가입 실패', err)
    })
  }

  // 로그인
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
      console.log('성공', res.data)
      token.value = res.data.key
      alert('로그인 되었습니다.')
      router.push({name: 'ArticleView'})
      getProfile()
      nickname.value = profileInfo.value.nickname
    })
    .catch((err)=>{
      console.log('실패', err)
    })
  }

  // 환율 데이터 DB에 저장하기
  const updateExchange = ()=>{
    axios({
      method: 'POST',
      url : `${API_URL}/api/v1/exchage/update/`,
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

    // 환율 데이터 가져오기
    const getExchange = ()=>{
      axios({
        method: 'GET',
        url : `${API_URL}/api/v1/exchage/`,
        headers:{
          Authorization: `Token ${token.value}`
        }
      })
      .then((res) =>{
        exchanges.value = res.data
        console.log('환율 데이터 가져오기 성공')
      })
      .catch((err)=>{
        console.log('환율 데이터 가져오기 실패', err)
      })
    }

  //로그 아웃
  const logout = () => {
    token.value = null
    nickname.value = null
    profileInfo.value = null
    localStorage.clear()
  }


  // 금융 데이터 DB에 저장하기
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

  // 금융 데이터 가져오기
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

  //
  

  return {posts, API_URL, getPosts, signUp, logIn,
     token, isLogin, getExchange, exchanges,
      logout,getFinanceSavingsProducts,
       getFinanceDepositsProducts, updateExchange,
        updateFinanceProducts, financeSavingsProducts,
         financeDepositsProducts, getProfile, profileInfo,
          updateProfile, nickname, getProfileLikes,
        profileLikes }
}, { persist: true })
