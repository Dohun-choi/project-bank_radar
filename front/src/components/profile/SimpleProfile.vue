<template>
  <div class="navbar-container">
    <div class="card p-4 custom-card">
      <a href="" @click.prevent="toProfile" class="list-group-item custom-link">
        <i class="bi bi-person"></i> 
        <p class="custom-text">'{{ userInfo?.nickname }}'님
          <br>반갑습니다.</p>
      </a>

      <template v-if="matchesTodayDate(userInfo?.birth)">
        <p class="custom-text">
          <i class="bi bi-cake"></i> {{ userInfo?.nickname }}님의 {{ userInfo?.age }}번째 생일을 축하드립니다!
        </p>
      </template>

      <div class="button-group d-flex flex-column">
        <button type="button" class="btn btn-success mb-2" @click="toNotify">
          <i class="bi bi-bell"></i> 알람
          <span v-if="notifies > 0" class="badge bg-danger">{{ notifies }}</span>
        </button>

        <button type="button" class="btn btn-primary mb-2" @click="toProfile">
          <i class="bi bi-person"></i> 프로필
        </button>

        <button type="button" class="btn btn-secondary" @click="store.logout">
          <i class="bi bi-box-arrow-right"></i> 로그아웃
        </button>
      </div>
    </div>
  </div>
</template>


<script setup>
import { useCounterStore } from '../../stores/counter';
import { onMounted, ref } from 'vue'
import axios from 'axios'
import router from '../../router';

const store = useCounterStore()
const notifies = ref(0)

onMounted(() => {
  if (store.isLogin) {
    axios({
      method: 'GET',
      url: `${store.API_URL}/api/v1/community/isnotify/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        console.log('notify 가져오기 성공', res);
        notifies.value = res.data.notifies
      })
      .catch((err) => {
        console.log('notify 가져오기 실패', err)
      })
  }
});

const userInfo = store.profileInfo

const matchesTodayDate = (dateString) => {
  const providedDate = new Date(dateString);
  const today = new Date();

  const providedMonth = providedDate.getMonth();
  const providedDay = providedDate.getDate();

  const todayMonth = today.getMonth();
  const todayDay = today.getDate();

  return providedMonth === todayMonth && providedDay === todayDay;
}

const toProfile = () => {
  router.push({ name: 'ProfileView' })
}

const toNotify = () => {
  router.push({ name: 'NofityView' })
}
</script>

<style scoped>
.custom-text {
  font-size: 30px; 
}
</style>
