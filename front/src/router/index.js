import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/community/ArticleView.vue'
import DetailView from '@/views/community/DetailView.vue'
import CreateView from '@/views/community/CreateView.vue'
import ModifyView from '@/views/community/ModifyView.vue'
import NofityView from '@/views/community/NofityView.vue'

import ProfileView from '@/views/accounts/ProfileView.vue'
import UpdateProfile from '@/components/profile/UpdateProfile.vue'
import Subscribes from '@/components/profile/Subscribes.vue'
import SignUpView from '@/views//accounts/SignUpView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import ExchangeMapView from '@/views/exchangeMap/ExchangeMapView.vue'

import RecommendItemView from '@/views/recommend/RecommendItemView.vue'
import RecommendTravelView from '@/views/recommend/RecommendTravelView.vue'

import FinanceDepositsView from '@/views/finance/FinanceDepositsView.vue'
import FinanceSavingsView from '@/views/finance/FinanceSavingsView.vue'
import SavingsDetail from '@/components/finance/SavingsDetail.vue'
import DepositsDetail from '@/components/finance/DepositsDetail.vue'


import MainView from '@/views/Main.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
        path: '/',
        name: 'MainView',
        component: MainView
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/post/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LoginView
    },
    {
      path: '/exchange/map',
      name: 'ExchangeMapView',
      component: ExchangeMapView
    },

    {
      path: '/post/modify/:id',
      name: 'ModifyView',
      component: ModifyView
    },
    {
      path: '/financeDeposits',
      name: 'FinanceDepositsView',
      component: FinanceDepositsView
    },
    {
      path: '/financeSavings',
      name: 'FinanceSavingsView',
      component: FinanceSavingsView
    },
    {
      path: '/savingsDetail/:key',
      name: 'SavingsDetail',
      component: SavingsDetail
    },
    {
      path: '/DepositsDetail/:key',
      name: 'DepositsDetail',
      component: DepositsDetail
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/updateprofile',
      name: 'UpdateProfile',
      component: UpdateProfile
    },
    {
      path: '/subscribes',
      name: 'Subscribes',
      component: Subscribes
    },
    {
      path: '/recommendTravel',
      name: 'RecommendTravelView',
      component: RecommendTravelView
    },
    {
      path: '/recommendItem',
      name: 'RecommendItemView',
      component: RecommendItemView
    },
    {
      path: '/notify',
      name: 'NofityView',
      component: NofityView
    },
  ]
})

// router.beforeEach((to, from)=>{
//   const store = useCounterStore()
//   if (to.name === 'ArticleView' && store.isLogin === false){
//     alert('로그인 ㄱ')
//     return {name: 'LogInView'}
//   }
//   if ((to.name === 'SignUpView' || to.name === 'LogInView') && store.isLogin){
//     alert('이미 로그인 했음')
//     return {name: 'ArticleView'}
//   }
// })

export default router