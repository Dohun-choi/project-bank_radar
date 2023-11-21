<template>
    <div>
        <div class="container mt-5">
        <div class="card mx-auto" style="max-width: 400px;">
            <img src="@/assets/purin.jpg" class="card-img-top rounded-circle" alt="프로필 이미지">
            <div class="card-body text-center">
            <h4 class="card-title">'{{ userInfo.nickname }}'님의 프로필</h4>
            <ul class="list-group list-group-flush">
                <li class="list-group-item">
                    <strong>생년월일:</strong> {{ userInfo.birth ? userInfo.birth.slice(0, 10) : null }}
                </li>
                <li class="list-group-item">
                    <strong>나이:</strong> {{ userInfo.age }}
                </li>
                <li class="list-group-item">
                    <strong>자산:</strong> {{ formatNumber(userInfo.assets) }}원
                </li>
                <li class="list-group-item">
                    <strong>월 수입:</strong> {{ formatNumber(userInfo.monthly_income) }}원
                </li>
                <li class="list-group-item">
                    <strong>나이 그룹:</strong> {{ userInfo.age_group }}
                </li>
                <li class="list-group-item">
                    <strong>월 수입 그룹:</strong> {{ Math.floor(userInfo.monthly_income_group) }}
                </li>
                <li class="list-group-item">
                    <strong>자산 그룹: </strong> {{ userInfo.assets_group }}
                </li>
            </ul>
            
    
            <button @click="updateProfile" class="btn btn-primary mt-3">프로필 수정</button>
    
            <button @click="goSubscribes" class="btn btn-primary mt-3">가입 내역 확인</button>
            </div>
        </div>
        </div>
    
    </div>
    </template>
    
    <script setup>
    import { useRouter } from 'vue-router';
    import { useCounterStore } from '../../stores/counter';
    
    const router = useRouter();
    const store = useCounterStore();
    
    const userInfo = store.profileInfo;
    
    const formatNumber = num => new Intl.NumberFormat().format(num)
    
    
    const updateProfile = () => router.push({ name: 'UpdateProfile' });
    
    const goSubscribes = () => router.push({ name: 'Subscribes' });
    </script>
    
    <style  scoped>
    button{
        margin: 10px;
    }
    </style>