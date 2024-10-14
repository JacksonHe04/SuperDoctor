<!-- PiniaButton.vue -->

<script setup>
// 导入userCounterStore函数
import { useCounterStore } from "@/stores/counter.js";
import {onMounted} from "vue";
// storeToRefs
import {storeToRefs} from "pinia";


// 执行方法得到store实例对象
const counterStore = useCounterStore();
console .log(counterStore);

// 方法包裹（只适用于数据处理）
const { count, doubleCount} = storeToRefs(counterStore);

// 方法直接从原来的counterStore中解构赋值
const { increment } = counterStore;

// action
onMounted(()=>{
  counterStore.getList();
})
</script>

<template>

  <div class="container">
    <button @click="increment">
      {{ count }}
    </button>
    {{ doubleCount }}
  </div>

</template>

<style scoped>
.container {
  display: flex;
  justify-content: center; /* 居中对齐 */
}
</style>
