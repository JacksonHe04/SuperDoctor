<script setup>
import LayoutHeader from "@/views/Layout/LayoutHeader.vue";
import LayoutFooter from "@/views/Layout/LayoutFooter.vue";
</script>

<template>
  <LayoutHeader />
  <!-- 二级路由出口 -->
  <RouterView />
  <LayoutFooter />
</template>
