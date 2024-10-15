<script setup>
import LayoutHeader from "@/views/Layout/LayoutHeader.vue";
import LayoutFooter from "@/views/Layout/LayoutFooter.vue";
import BackToTop from "@/views/Layout/BackToTop.vue";
</script>

<template>
  <LayoutHeader />
  <!-- 二级路由出口 -->
  <RouterView />
  <BackToTop />
  <LayoutFooter />
</template>
