<template>
    <div>
        <form @submit.prevent="modify">
            <div>
                <label for="title">제목 변경</label>
                <input type="text" id="title" v-model="title">
            </div>
            <div>
                <label for="content">내용 변경</label>
                <input type="text" id="content" v-model="content">
            </div>
            <input type="submit" value="수정하기">
        </form>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '../../stores/counter';

const store = useCounterStore()
const router = useRouter()
const route = useRoute()
const query = route.query
const title = ref(query.title)
const content = ref(query.content)

const modify = () => {
    axios({
        method: 'PUT',
        url: `${store.API_URL}/api/v1/community/posts/${route.params.id}/`,
        data : {
            title: title.value ? title.value : query.title,
            content: content.value ? content.value : query.content
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
.then((res)=>{
    console.log('성공')
    router.push({name: 'DetailView'})
})
.catch((err)=>{
    console.log('실패', err)
}) 
}

</script>


<style scoped>

</style>
