<script setup>
  import { useCounterStore } from '../../stores/counter';
  import { onMounted, ref } from 'vue'
  import axios from 'axios'
import router from '../../router';

  const store = useCounterStore()
  const notifies = ref(0)

  onMounted(() => {
  if(store.isLogin){
    axios({
          method: 'GET',
          url: `${store.API_URL}/api/v1/community/isnotify/`,
          headers: {
              Authorization: `Token ${store.token}`
          }
      })
      .then((res)=>{
          console.log('notify 가져오기 성공', res);
          notifies.value = res.data.notifies
      })
      .catch((err)=>{
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
    router.push({name: 'ProfileView'})
  }

  const toNotify = () => {
    router.push({name: 'NofityView'})
  }
</script>

<template>
  <div>
    <div>
      <div class="card p-0">
        <a href="" @click.prevent="toProfile"
          class="list-group-item"
          style="display: inline-block;
                  color: lab(46.05 58.95 17.38);">
          {{ userInfo.nickname }}
        </a>님 반갑습니다.
        <template v-if="matchesTodayDate(userInfo.birth)">
          <p>{{ userInfo.nickname }}님의 {{ userInfo.age }}번째 생일을 축하드립니다!</p>
        </template>

        <div class="button-group">
          <button type="button" class="btn btn-outline-success position-relative btn-sm" @click="toNotify">
            알람
            <span v-if="notifies > 0" class="position-absolute top-0 start-100 translate-middle p-2 bg-danger border border-light rounded-circle">
              <span class="visually-hidden">{{ notifies }}</span>
            </span>
          </button>
          <button type="button" class="btn btn-outline-primary btn-sm" @click="toProfile">
              프로필
          </button>
          <button type="button" class="btn btn-outline-secondary btn-sm" @click="store.logout">
            로그아웃
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
.button-group {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.member {
  white-space: nowrap;
}
</style>
