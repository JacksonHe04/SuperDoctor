<template>
  <div class="hero-section">
    <div class="container">
      <h1 class="title">Super Doctor</h1>
      <p class="subtitle">Based on Natural Language Process</p>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeTitle'
}
</script>

<style scoped>
.hero-section {
  display: flex;
  justify-content: center;
  //align-items: center;
  min-height: calc(100vh - 60px);
  height: auto; /* 假设导航栏高度为60px */
  background-color: #f5f5f5; /* 背景颜色 */
}

.container {
  text-align: center;
  margin-top: 120px;
}

.title {
  font-size: 4rem;
  color: #333;
  margin-bottom: 0.5em;
}

.subtitle {
  font-size: 1.5rem;
  color: $greyColor2;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .title {
    font-size: 3rem;
  }

  .subtitle {
    font-size: 1.2rem;
  }
}
</style>
