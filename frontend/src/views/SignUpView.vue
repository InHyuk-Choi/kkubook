<template>
  <div class="min-h-screen flex items-center justify-center bg-[#fffdf8] px-4">
    <div class="bg-white shadow-lg p-12 rounded-2xl w-full max-w-lg space-y-8 border">
      <h2 class="text-3xl font-extrabold text-center text-[#444]">회원가입</h2>

      <form @submit.prevent="signup" class="space-y-5">
        <input v-model="auth.username" placeholder="아이디" class="input" />
        <input v-model="auth.nickname" placeholder="닉네임" class="input" />
        <input v-model="auth.password1" type="password" placeholder="비밀번호" class="input" />
        <input v-model="auth.password2" type="password" placeholder="비밀번호 확인" class="input" />
        <button type="submit" class="submit-btn">회원가입</button>
      </form>
    </div>
  </div>
</template>
<script setup>
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
const router = useRouter()
const signup = () => auth.signup(router, Swal)
</script>

<style>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
}

.custom-ok-button-blue {
  opacity: 1 !important;
  background-color: #3b82f6 !important;
  color: white !important;
  font-weight: 600;
  border-radius: 0.375rem;
  padding: 0.5rem 1rem;
  transition: all 0.2s ease-in-out;
  box-shadow: none !important;
}

.custom-ok-button-blue:hover {
  transform: scale(1.08);
  background-color: #2563eb !important;
}

.custom-ok-button-red {
  opacity: 1 !important;
  background-color: #ef4444 !important;
  color: white !important;
  font-weight: 600;
  border-radius: 0.375rem;
  padding: 0.5rem 1rem;
  transition: all 0.2s ease-in-out;
  box-shadow: none !important;
}

.custom-ok-button-red:hover {
  transform: scale(1.08);
  background-color: #dc2626 !important;
}

.input {
  @apply w-full border rounded-lg p-4 text-base focus:outline-none focus:ring focus:ring-yellow-300;
}

.submit-btn {
  @apply w-full bg-yellow-400 text-white font-bold py-3 rounded-lg hover:bg-yellow-500 transition text-lg;
}
</style>
