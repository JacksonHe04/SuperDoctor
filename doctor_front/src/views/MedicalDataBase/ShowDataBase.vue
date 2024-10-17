<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';

const currentPage = ref(1);
const pageSize = 10; // 每页显示10条数据
const totalData = ref([]);
const paginatedData = ref([]);
const selectedDataset = ref('');

onMounted(() => {
  selectedDataset.value = 'train'; // 确保页面加载后有默认值
});


// 监听selectedDataset的变化，并获取相应数据集
watch(selectedDataset, async (newDataset) => {
  console.log('selectedDataset changed:', newDataset); // 添加日志
  if (newDataset) {
    await fetchDataset(newDataset);
  }
});

// 获取数据集函数
const fetchDataset = async (dataset) => {
  console.log('Fetching dataset:', dataset);  // 添加日志
  try {
    const response = await axios.get('http://localhost:8000/restapi/get-dataset/', { dataset });
    console.log('Data fetched successfully:', response.data);  // 添加日志
    totalData.value = response.data;
    currentPage.value = 1;
    updatePagination();
  } catch (error) {
    console.error('获取数据集失败:', error);
  }
};


// 分页更新函数
const updatePagination = () => {
  const start = (currentPage.value - 1) * pageSize;
  const end = start + pageSize;
  paginatedData.value = totalData.value.slice(start, end);
};

// 监听当前页的变化，更新分页数据
watch(currentPage, () => {
  updatePagination();
});

// 前一页
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

// 后一页
const nextPage = () => {
  if (currentPage.value * pageSize < totalData.value.length) {
    currentPage.value++;
  }
};
</script>

<template>
  <div id="dynamic-component" class="dynamic-component">
    <h2>数据集表格 - {{ selectedDataset }}</h2>
    <table>
      <thead>
      <tr>
        <th>编号 (id)</th>
        <th>语句 (s)</th>
        <th>症状 (h)</th>
        <th>疾病 (t)</th>
        <th>临床表现 (r)</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(result, index) in paginatedData" :key="index">
        <td>{{ result.auto_id }}</td>
        <td>{{ result.sentence }}</td>
        <td>{{ result.h }}</td>
        <td>{{ result.t }}</td>
        <td>{{ result.r }}</td>
      </tr>
      </tbody>
    </table>

    <!-- 分页按钮 -->
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
      <span>当前页: {{ currentPage }}</span>
      <button @click="nextPage" :disabled="currentPage * pageSize >= totalData.length">下一页</button>
    </div>
  </div>
</template>

<style scoped>
.dynamic-component {
  margin-top: 20px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
  text-align: center;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

table, th, td {
  border: 1px solid black;
}

th, td {
  padding: 10px;
  text-align: center;
}

.pagination {
  margin-top: 10px;
}
</style>
