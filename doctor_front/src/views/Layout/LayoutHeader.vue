<!-- LayoutHeader.vue -->
<script setup>

</script>

<template>
  <header class='app-header'>
    <div class="container">
      <h1 class="logo">
        <RouterLink to="/">
          <img src="@/assets/images/sd_logo.png" alt="Logo" />
        </RouterLink>
      </h1>
      <ul class="app-header-nav">
        <li class="home">
          <RouterLink to="/">首页</RouterLink>
        </li>
        <li> <RouterLink to="/MedicalDatabase" active-class="active">医疗数据库</RouterLink> </li>
        <li> <RouterLink to="/nlp" active-class="active">自然语言处理</RouterLink> </li>
        <li> <RouterLink to="/login" active-class="active">登录</RouterLink> </li>
      </ul>
    </div>
  </header>
</template>


<style scoped lang='scss'>
.app-header {
  background: #fff;
  border-bottom: 2px solid #e0e0e0; // 添加灰色下边框
  // position: fixed; // 固定位置
  // top: 0; // 置顶
  // width: 100%; // 确保宽度覆盖整个屏幕

  .container {
    display: flex;
    align-items: center;
  }

  .logo {
    width: 300px;
    margin-left: 40px;

    a {
      display: block;
      // height: 132px; // 根据实际图片大小调整
      height: auto;
      width: 100%;
      margin: 0 auto;
    }
  }

  .app-header-nav {
    width: 450px;
    display: flex;
    padding-left: 0;
    position: relative;
    z-index: 998;
    margin-left: auto;

    li {
      text-align: center;

      &::after { // 添加分隔线
        content: "";
        display: inline-block;
        width: 1px; // 分隔线宽度
        height: 90%; // 分隔线高度略小于容器
        background-color: #e0e0e0; // 灰色分隔线
        vertical-align: bottom; // 垂直居中对齐
        margin-left: 20px; // 分隔线与下一个li之间的间距
        margin-right: 20px;
      }

      a {
        font-size: 16px;
        line-height: 32px;
        height: 32px;
        display: inline-block;
        // 加粗
        font-weight: bold;
        // color: $greyColor2;

        &:hover {
          color: $xtxColor;
          border-bottom: 1px solid $xtxColor;
        }

        &.active {
          color: $xtxColor;
          border-bottom: 1px solid $xtxColor;
        }

      }

      &:last-child::after { // 移除最后一个li后的分隔线
        content: none;
      }
    }
  }
}
</style>