<script setup>
import {ref} from 'vue';
import ShowDataBase from '@/views/MedicalDataBase/ShowDataBase.vue'; // 引入动态组件

const showComponent = ref(false);
const selectedDataset = ref('');

const handleButtonClick = (datasetName) => {
  selectedDataset.value = datasetName;
  showComponent.value = true;
  setTimeout(() => {
    const componentElement = document.getElementById('dynamic-component');
    if (componentElement) {
      componentElement.scrollIntoView({behavior: 'smooth'});
    }
  }, 100);
};
</script>

<template>
  <div class="card-container">
    <div class="card">
      <div class="title-1">训练集</div>
      <div class="content">7,000</div>
      <button class="btn" @click="handleButtonClick('train')">查看数据集</button>
      <div class="bar">
        <div class="emptybar"></div>
        <div class="filledbar"></div>
      </div>
    </div>

    <div class="card">
      <div class="title-1">验证集</div>
      <div class="content">2,000</div>
      <button class="btn" @click="handleButtonClick('val')">查看数据集</button>
      <div class="bar">
        <div class="emptybar"></div>
        <div class="filledbar"></div>
      </div>
    </div>

    <div class="card">
      <div class="title-1">测试集</div>
      <div class="content">1,000</div>
      <button class="btn" @click="handleButtonClick('test')">查看数据集</button>
      <div class="bar">
        <div class="emptybar"></div>
        <div class="filledbar"></div>
      </div>
    </div>
  </div>

  <!-- 展示动态组件 -->
  <ShowDataBase v-if="showComponent" :selectedDataset="selectedDataset"/>
</template>

<style scoped lang="scss">
/* 现有样式保持不变 */
.card-container {
  display: flex;
  margin-top: 50px;
  justify-content: center;
  align-items: center;
  gap: 50px; /* 卡片之间的间距 */
}

.card {
  display: flex;
  height: 280px;
  width: 200px;
  background-color: $themeTrans;
  border-radius: 20px;
  box-shadow: -1rem 0 3rem #00000044;
  transition: 0.4s ease-out;
  position: relative;
  left: 0;
}

.card:hover {
  transform: translateY(-20px);
  transition: 0.4s ease-out;
  text-shadow: 2px 2px 8px $themeColor;
}

.card:hover ~ .card {
  position: relative;
  left: 50px;
  transform: rotateX(-15deg) rotateY(10deg);
  transition: 0.4s ease-out;
}

.title-1 {
  color: #ffffff;
  font-size: 28px;
  font-weight: 800;
  position: absolute;
  left: 20px;
  top: 15px;
}

.btn {
  position: absolute;
  top: 195px;
  margin: 0 20px;
  width: 120px;
  height: 32px;
  border-radius: 8px;
  border: 2px solid $themeColor;
  background-color: #ffffff;
  color: $greyColor2;
  transition: 0.4s ease-out;
  cursor: pointer;
  font-weight: bold;
}

.btn:hover {
  transition: 0.4s ease-out;
  background-color: $themeBold;
  color: #ffffff;
  box-shadow: 0px 0px 20px $themeColor;
}

.bar {
  position: relative;
  top: 250px;
  height: 5px;
  width: 100%;
}

.emptybar {
  background-color: $greyColor;
  width: 100%;
  height: 100%;
}

.filledbar {
  position: absolute;
  top: 0px;
  z-index: 3;
  width: 0px;
  height: 100%;
  background: $themeColor;
  background: linear-gradient(90deg, $themeBold, $themeLight 100%);
  transition: 0.6s ease-out;
}

.card:hover .filledbar {
  width: 100%;
  transition: 0.4s ease-out;
}

.content {
  position: absolute;
  padding: 20px;
  top: 60px;
  color: white;
  font-size: 3.2rem;
  font-weight: bold;
}

.stroke {
  stroke: white;
  stroke-dasharray: 360;
  stroke-dashoffset: 360;
  transition: 0.6s ease-out;
}

.card:hover .stroke {
  stroke-dashoffset: 100;
  transition: 0.6s ease-out;
}

.dynamic-component {
  margin-top: 50px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
  text-align: center;
}
</style>
