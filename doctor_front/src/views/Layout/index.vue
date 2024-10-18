<script setup>
import LayoutHeader from "@/views/Layout/LayoutHeader.vue";
import HomeTitle from "@/views/Layout/TitleAndBackground.vue";
import LayoutFooter from "@/views/Layout/LayoutFooter.vue";
import BackToTop from "@/views/Layout/BackToTop.vue";
</script>

<template>
  <LayoutHeader />
  <HomeTitle>
    <RouterView />
  </HomeTitle>
  <BackToTop />
  <LayoutFooter />
</template>
