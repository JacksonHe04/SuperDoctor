<!-- doctor_front/src/views/Home/SearchDataBase.vue -->
<template>
  <div class="search-database">
    <div class="box-card">
      <h2>请选择数据集并搜索医疗数据</h2>
      <!-- 添加数据集选择器 -->
      <label for="dataset-select"></label>
      <select id="dataset-select" v-model="selectedDataset">
        <option value="train">Train 训练集</option>
        <option value="val">Val 验证集</option>
        <option value="test">Test 测试集</option>
      </select>

      <!-- 搜索表单 -->
      <form @submit.prevent="searchDatabase">
        <input type="text" v-model="searchQuery" placeholder="请输入症状或表现等..." class="search-input" />
        <button type="submit" class="search-button">搜索</button>
      </form>

      <!-- 显示查询结果 -->
      <table v-if="searchResults.length" class="search-results">
        <thead>
        <tr>
          <th style="width: 34%">头实体 (h)</th>
          <th style="width: 34%">尾实体 (t)</th>
          <th style="width: 32%">医疗关系 (r)</th>
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

      <p v-else-if="hasSearched" class="no-data">暂无数据，请输入有效的搜索关键词。</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: '',       // 用户输入的查询
      selectedDataset: 'train',  // 选中的数据集（默认为 train）
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

      // 发送请求到后端获取搜索结果，并包含所选数据集的信息
      axios.post(`http://localhost:8000/restapi/search/`, {
        query: this.searchQuery,
        dataset: this.selectedDataset  // 发送所选数据集到后端
      })
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

<style scoped lang="scss">
.search-database {
  max-width: 600px;
  margin: 0 auto;
  padding: 50px;
}
h2 {
  text-align: center;
  font-weight: 800;
  color: darkgrey;
}

select {
  padding: 5px;
  margin-top: 15px;
  border-radius: 20px;
  border-style: solid;
  border-width: 2px 2px 2px 2px;
  border-color: $themeTrans;
  transform: translate(0px, 0px) rotate(0deg);
  transition: 0.2s;
  box-shadow: -4px -2px 16px 0px #ffffff, 4px 2px 16px 0px rgba(180, 203, 181, 0.6);
  font-weight: bold;
  color: grey;
  outline: none;
}

select:focus-visible {
  border-color: $themeColor; /* 修改为所需的边框颜色 */
}

form {
  margin-top: 20px;
}
.search-input {
  height: 46.5px;
  width: calc(100% - 120px);
  padding: 18px;
  font-size: medium;
  margin-right: 10px;
  border-radius: 50px;
  border-style: solid;
  border-width: 2px 2px 2px 2px;
  border-color: $themeTrans;
  transform: translate(0px, 0px) rotate(0deg);
  transition: 0.2s;
  box-shadow: -4px -2px 16px 0px #ffffff, 4px 2px 16px 0px rgba(180, 203, 181, 0.6);

  // border-radius: 40px 40px 40px 40px;
}
/* From Uiverse.io by barisdogansutcu */
.search-button {
  //display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-family: inherit;
  font-size: 16px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.4px;
  color: $greyColor2;
  background-color: $themeTrans;
  border-style: solid;
  border-width: 2px 2px 2px 2px;
  border-color: rgba(255, 255, 255, 0.333);
  border-radius: 40px 40px 40px 40px;
  padding: 10px 25px 10px 25px;
  transform: translate(0px, 0px) rotate(0deg);
  transition: 0.2s;
  box-shadow: -4px -2px 16px 0px #ffffff, 4px 2px 16px 0px rgba(180, 203, 181, 0.6);
  cursor: pointer;
}

.search-button:hover {
  color: #516d91;
  background-color: $themeColor;
  box-shadow: -2px -1px 8px 0px #ffffff, 2px 1px 8px 0px rgb(95 157 231 / 48%);
}

.search-button:active {
  box-shadow: none;
}
.search-results {
  margin-top: 20px;
  width: 100%;
  border-radius: 20px;
  border-collapse: collapse;
  background-color: $themeTrans3;
  border: 1px solid transparent;
  overflow: hidden;
}

.search-results th {
  background-color: $themeTrans;
  color: grey;
  font-weight: bold;
  text-align: left;
  padding: 12px 0 12px 20px;
}

.search-results th, .search-results td {
  border: 1px solid #ddd;
  padding: 8px 0 8px 20px;
  text-align: left;
}
.no-data {
  text-align: center;
  color: #999;
}
</style>
