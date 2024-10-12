<template>
  <div>
    <h2>所有医疗数据</h2>
    <div v-if="allData && allData.length > 0">
      <div v-for="(data, index) in allData" :key="index" class="medical-data">
        <p><strong>症状:</strong> {{ data.symptom }}</p>
        <p><strong>诊断:</strong> {{ data.diagnosis }}</p>
        <p><strong>治疗方法:</strong> {{ data.treatment }}</p>
        <p><strong>药物建议:</strong> {{ data.medication }}</p>
        <hr />
      </div>
    </div>
    <div v-else>
      <p>没有可显示的医疗数据。</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      allData: []  // 存储所有从后端获取的数据
    };
  },
  created() {
    // 在组件创建时调用 getAllData 方法
    this.getAllData();
  },
  methods: {
    getAllData() {
      axios.get('http://localhost:8000/restapi/all_data/')  // 向后端发送 GET 请求
          .then(response => {
            this.allData = response.data;  // 将获取的数据赋值给 allData
          })
          .catch(error => {
            console.error("Error fetching all data:", error);
          });
    }
  }
}
</script>

<style scoped>
.medical-data {
  margin-bottom: 1.5rem;
}
</style>