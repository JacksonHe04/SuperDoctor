<!-- doctor_front/src/views/Home/SearchDataBase.vue -->
<template>
  <div class="search-database">
    <div class="box-card">
      <h2>在Train中搜索医疗数据</h2>
      <form @submit.prevent="searchDatabase">
        <input type="text" v-model="searchQuery" placeholder="请输入症状或表现等..." class="search-input" />
        <button type="submit" class="search-button">搜索</button>
      </form>

      <table v-if="searchResults.length" class="search-results">
        <thead>
          <tr>
            <th>症状 (h)</th>
            <th>疾病 (t)</th>
            <th>临床表现 (r)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(result, index) in searchResults" :key="index">
            <td>{{ result.h }}</td>
            <td>{{ result.t }}</td>
            <td>{{ result.r }}</td>
          </tr>
        </tbody>
      </table>

      <p v-else-if ="hasSearched" class="no-data">暂无数据，请输入有效的搜索关键词。</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: '',       // 用户输入的查询
      searchResults: [],     // 查询到的数据结果
      hasSearched: false     // 是否已进行过搜索
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
        alert("请输入有效的搜索关键词！");
        return;
      }

      // 发送请求到后端获取搜索结果
      axios.post(`http://localhost:8000/restapi/search/`, { query: this.searchQuery })
          .then((response) => {
            console.log(response.data);  // 打印后端返回的结果
            this.searchResults = response.data.results;  // 假设后端返回的JSON格式为 {results: [...]}
            this.hasSearched = true;
          })
          .catch((error) => {
            alert("搜索过程中发生错误，请稍后再试。");
            this.hasSearched = false;
          });
    }
  }
};
</script>

<style scoped>
.search-database {
  max-width: 600px;
  margin: 0 auto;
  padding: 50px;
}
h2 {
  text-align: center;
  //color: $;
}
form {
  margin-top: 20px;
}
.search-input {
  width: calc(100% - 120px);
  padding: 10px;
  margin-right: 10px;
}
.search-button {
  padding: 10px 20px;
  background-color: #b4cbb5;
  color: white;
  border: none;
  cursor: pointer;
}
.search-results {
  margin-top: 20px;
  width: 100%;
  border-collapse: collapse;
}
.search-results th, .search-results td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
.no-data {
  text-align: center;
  color: #999;
}
</style>
