<template>
  <div class="relative h-screen overflow-hidden bg-[#fffdf8]">

    <!-- 🧷 상단 고정된 아이콘 바 -->
<div class="fixed top-0 w-full grid grid-cols-3 items-center px-6 py-2 z-50 bg-[#fffdf8]">
    <div class="flex justify-start">
      <img
        src="/bookcase.png"
        class="w-10 h-10 object-contain hover:scale-110 transition-transform mt-[-4px] cursor-pointer"
        @click="router.push({ name: 'RecommendedBooks' })"
      />
      </div>
      <div class="flex justify-center">
      <img src="/favicon.png" alt="logo" class="w-28 h-20 object-contain" />
      </div>
      <div class="flex justify-end gap-6 items-center">
      <div class="flex gap-6 items-center">
        </div>
          <div>
    <!-- 📦 보관함 버튼 -->
    <img
      src="/box.png"
      alt="보관함"
      class="w-10 h-10 object-contain cursor-pointer hover:scale-110 transition-transform"
      @click="openInventory"
    />
            
    <!-- 📦 보관함 사이드바 -->
    <InventorySidebar
  :isOpen="showInventory"
  :foodBasic="auth.basicFood"
  :foodPremium="auth.premiumFood"
  @close="showInventory = false"
/>
  </div>
        <img src="/cart.png" alt="상점" class="w-10 h-10 object-contain hover:scale-110 transition-transform cursor-pointer" @click="router.push({ name: 'store' })" />
      </div>
    </div>

    <!-- 📦 본문 콘텐츠: 수직 중앙 배치 -->
<main
      class="absolute top-[88px] bottom-[64px] left-0 right-0 flex justify-center items-center overflow-y-auto">
          <div class="flex flex-col items-center gap-4 transform scale-[0.85] sm:scale-[0.9] md:scale-100 origin-center">
      <PetStatus />
      <LevelInfo />
      </div>
    </main>
    
    <!-- 🔒 하단 고정 바텀 네브바 -->

  </div>

</template>

<script setup>
import PetStatus from '@/components/PetStatus.vue'
import LevelInfo from '@/components/LevelInfo.vue'

import { useRouter } from 'vue-router'
import { ref } from 'vue'
import InventorySidebar from '@/components/InventorySidebar.vue'
import { useAuthStore } from '@/stores/auth'



const auth = useAuthStore()

const router = useRouter()
const showInventory = ref(false)
const openInventory = () => {
  showInventory.value = true
}


</script>