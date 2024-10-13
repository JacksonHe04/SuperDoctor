<!-- Container.vue -->
<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <NavHeader />
      </el-header>
      <el-container>
        <el-main>
          <SearchDataBase />
        </el-main>
        <el-footer>
          <LayoutFooter />
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import NavHeader from "@/components/NavHeader.vue";
import SearchDataBase from "@/components/SearchDataBase.vue";
import LayoutFooter from "@/components/LayoutFooter.vue";
</script>

<style>
.common-layout {
  display: flex;
  flex-direction: column;
  width: 100%;
  min-width: 80vw; /* 确保至少占据整个视口宽度 */
  box-sizing: border-box; /* 包含padding和border在内 */
}

el-container {
  width: 100%; /* 确保容器宽度为100% */
}

</style>
