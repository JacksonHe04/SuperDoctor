<!-- doctor_front/src/components/SearchDataBase.vue -->
<template>
  <div class="search-database">
    <el-card class="box-card">
      <h2>在Train中搜索医疗数据</h2>
      <el-form :inline="true" @submit.prevent="searchDatabase">
        <el-form-item>
          <el-input v-model="searchQuery" placeholder="请输入症状或表现等..." clearable />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="searchDatabase">搜索</el-button>
        </el-form-item>
      </el-form>

      <el-table v-if="searchResults.length" :data="searchResults" style="width: 100%">
        <el-table-column prop="h" label="症状 (h)" />
        <el-table-column prop="t" label="疾病 (t)" />
        <el-table-column prop="r" label="临床表现 (r)" />
      </el-table>

      <el-alert v-else type="info" title="暂无数据，请输入有效的搜索关键词。" />
    </el-card>
  </div>
</template>

<script>
import { ElMessage } from 'element-plus';
import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: '',       // 用户输入的查询
      searchResults: []      // 查询到的数据结果
    };
  },
  methods: {
    /**
     * 搜索数据库方法
     * 当用户点击搜索按钮时，此方法将被调用
     * 它负责检查搜索查询的有效性，并向后端发送请求以获取搜索结果
     */
    searchDatabase() {
      // 检查搜索查询是否为空或仅包含空格
      if (!this.searchQuery.trim()) {
        ElMessage.warning("请输入有效的搜索关键词！");
        return;
      }

      // 发送请求到后端获取搜索结果
      axios.post(`http://localhost:8000/restapi/search/`, { query: this.searchQuery })
          .then((response) => {
            console.log(response.data);  // 打印后端返回的结果
            this.searchResults = response.data.results;  // 假设后端返回的JSON格式为 {results: [...]}
          })
          .catch((error) => {
            ElMessage.error("搜索过程中发生错误，请稍后再试。");
          });

    }
  }
};

</script>

<style scoped>
.search-database {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
h2 {
  text-align: center;
  color: #409EFF;
}
</style>
