<!-- NavHeader.vue -->
<template>
  <!-- 导航栏组件，使用 Element UI 的菜单组件构建 -->
  <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
  >
    <!-- 导航栏项，包含公司 logo -->
    <el-menu-item index="0">
      <img
          style="width: 100px"
          src="../assets/images/sd_logo.png"
          alt="SuperDoctor Logo"
      />
    </el-menu-item>
    <!-- 导航栏项，显示“Processing Center” -->
    <el-menu-item index="1">Processing Center</el-menu-item>
    <!-- 导航栏项，包含“Workspace”的子菜单 -->
    <el-sub-menu index="2">
      <template #title>Workspace</template>
      <!-- 子菜单项 -->
      <el-menu-item index="2-1">item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
      <!-- 嵌套子菜单 -->
      <el-sub-menu index="2-4">
        <template #title>item four</template>
        <!-- 嵌套子菜单项 -->
        <el-menu-item index="2-4-1">item one</el-menu-item>
        <el-menu-item index="2-4-2">item two</el-menu-item>
        <el-menu-item index="2-4-3">item three</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
  </el-menu>
</template>

<script lang="ts" setup>
// 导入 Vue 的 ref 函数
import { ref } from 'vue'

// 定义一个 ref 变量，用于存储当前激活的菜单项索引
const activeIndex = ref('1')

/**
 * 处理菜单项点击事件
 * @param key 点击的菜单项的索引
 * @param keyPath 点击的菜单项的索引路径
 */
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<!-- 样式，设置导航栏左侧第一个菜单项右边界自动布局 -->
<style>
.el-menu--horizontal > .el-menu-item:nth-child(1) {
  margin-right: auto;
}
</style>
