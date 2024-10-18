<!-- ShowDataBase.vue -->
<script setup>
import { ref, watch, onMounted } from 'vue';
import axios from 'axios';

/**
 * 定义组件的属性
 *
 * @param {Object} defineProps - 一个函数，用于定义组件接收的属性
 * @property {String} selectedDataset - 所选数据集的标识符，这是一个必填项
 */
const props = defineProps({
  selectedDataset: {
    type: String,
    required: true
  },
  selectedDataCh: {
    type: String,
    required: true
  }
});


const currentPage = ref(1);
const pageSize = 10;
const totalData = ref([]);
const paginatedData = ref([]);
const totalPages = ref(0);
const goToPage = ref(1);


watch(() => props.selectedDataset, async (newDataset) => {
  // 当selectedDataset变化时，调用fetchDataset函数获取新的数据集
  if (newDataset) {
    console.log('已监听成功:', newDataset);
    await fetchDataset(newDataset);
  }
});

/**
 * 异步获取指定的数据集
 * @param {String} dataset - 需要获取的数据集类型，可为'train', 'val', 或 'test'
 */
const fetchDataset = async (dataset) => {
  // 初始化URL，根据不同的数据集类型选择不同的API endpoint
  let url = '';
  switch (dataset) {
    case 'train':
      url = 'http://localhost:8000/restapi/get-trainset/';
      break;
    case 'val':
      url = 'http://localhost:8000/restapi/get-valset/';
      break;
    case 'test':
      url = 'http://localhost:8000/restapi/get-testset/';
      break;
    default:
      // 如果数据集类型未知，打印错误信息并终止函数执行
      console.error('未知的数据集类型:', dataset);
      return;
  }

  try {
    // 发起GET请求，获取数据集
    const response = await axios.get(url);
    // 更新总数据，当前页码重置为第1页
    totalData.value = response.data;
    currentPage.value = 1;
    // 根据总数据量和每页大小计算总页数
    totalPages.value = Math.ceil(totalData.value.length / pageSize);
    // 更新分页信息
    updatePagination();
    console.log('已发送请求:', dataset);
  } catch (error) {
    // 如果获取数据集失败，打印错误信息
    console.error('获取数据集失败:', error);
  }
};

// 组件挂载时立即调用 fetchDataset
onMounted(async () => {
  if (props.selectedDataset) {
    await fetchDataset(props.selectedDataset);
  }
});

const updatePagination = () => {
  const start = (currentPage.value - 1) * pageSize;
  const end = start + pageSize;
  paginatedData.value = totalData.value.slice(start, end);
};

// 分页控制
watch(currentPage, updatePagination);

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
  goToPage.value = currentPage.value;
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
  goToPage.value = currentPage.value;
};

const jumpToPage = () => {
  if (goToPage.value >= 1 && goToPage.value <= totalPages.value) {
    currentPage.value = goToPage.value;
  }
};
</script>

<template>
  <div id="dynamic-component" class="dynamic-component">
    <h2>数据集表格 - {{ props.selectedDataCh }}</h2>
    <table>
      <thead>
      <tr>
        <th style="width: 5%">编号</th>
        <th style="width: 55%">语句 (s)</th>
        <th style="width: 15%">头实体 (h)</th>
        <th style="width: 15%">尾实体 (t)</th>
        <th style="width: 10%">医疗关系 (r)</th>
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

    <!-- 分页部分 -->
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
      <span>显示第 {{ (currentPage - 1) * pageSize + 1 }} 到第 {{ Math.min(currentPage * pageSize, totalData.length) }} 条，共 {{ totalData.length }} 条数据</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">下一页</button>

      <!-- 跳转到指定页 -->
      <div class="page-jump">
        <label for="pageInput">跳转到页:</label>
        <input type="number" v-model="goToPage" id="pageInput" min="1" :max="totalPages" @keyup.enter="jumpToPage" />
        <button @click="jumpToPage">跳转</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.dynamic-component {
  margin-top: 50px;
  padding: 20px;
  background-color: $greyTrans;
  text-align: center;
}

h2 {
  font-size: 28px;
  padding: 10px;
  font-weight: 800;
  color: grey;
}

table {
  width: 70%;
  border-collapse: collapse;
  margin: 20px auto;
  background-color: $themeTrans3;
  border: 1px solid transparent;
  border-radius: 20px;
  overflow: hidden;
}

th {
  background-color: $themeTrans;
  color: grey;
  font-weight: bold;
  text-align: left;
  padding: 12px 0 12px 20px;
}

th, td {
  border: 1px solid $greyNoraml;
}

th, td {
  padding: 10px;
  text-align: center;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  color: $darkGreen;

  button {
    background-color: $themeColor;
    border: none;
    color: white;
    padding: 5px 10px;
    margin: 0 10px;
    border-radius: 5px;
    cursor: pointer;

    &:disabled {
      background-color: $greyColor2;
      cursor: not-allowed;
    }
  }

  .page-jump {
    display: flex;
    align-items: center;
    margin-left: 20px;

    label {
      margin-right: 10px;
    }

    input {
      width: 50px;
      padding: 5px;
      text-align: center;
      border-radius: 5px;
      border: 1px solid $greyColor2;
    }

    button {
      background-color: $themeColor;
      border: none;
      color: white;
      padding: 5px 10px;
      border-radius: 5px;
      cursor: pointer;
    }
  }
}
</style>
