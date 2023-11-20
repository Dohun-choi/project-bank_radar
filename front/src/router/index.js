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
import MapView from '@/views/map/MapView.vue'
import ExchangeView from '@/views/exchange/ExchangeView.vue'
import RecomandView from '@/views/recomand/RecomandView.vue'

import FinanceView from '@/views/finance/FinanceView.vue'
import SavingsDetail from '@/components/finance/SavingsDetail.vue'
import DepositsDetail from '@/components/finance/DepositsDetail.vue'

import { useCounterStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
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
      path: '/map',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/exchange',
      name: 'ExchangeView',
      component: ExchangeView
    },
    {
      path: '/post/modify/:id',
      name: 'ModifyView',
      component: ModifyView
    },
    {
      path: '/finance',
      name: 'FinanceView',
      component: FinanceView
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
      path: '/recomand',
      name: 'RecomandView',
      component: RecomandView
    },
    {
      path: '/notify',
      name: 'NofityView',
      component: NofityView
    }
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
