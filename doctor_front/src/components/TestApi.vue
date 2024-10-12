<!-- doctor_front/src/components/TestApi.vue -->
<template>
  <div>
    <h2>查询症状</h2>
    <input v-model="symptom" placeholder="输入症状">
    <button @click="querySymptom">查询</button>

    <h3>查询结果</h3>
    <div v-if="result">
      <p>症状: {{ result.symptom }}</p>
      <p>诊断: {{ result.diagnosis }}</p>
      <p>治疗方法: {{ result.treatment }}</p>
      <p>药物建议: {{ result.medication }}</p>
    </div>
    <div v-else-if="error">
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      symptom: '',  // 输入的症状
      result: null, // 查询的结果
      error: null   // 错误信息
    };
  },
  methods: {
    querySymptom() {
      axios.post('http://localhost:8000/restapi/query_symptom/', {symptom: this.symptom})
          .then(response => {
            if (response.data.length) {
              this.result = response.data[0];  // 假设后端返回多个结果时，取第一个
              this.error = null;
            } else {
              this.result = null;
              this.error = "没有找到相关的医疗信息";
            }
          })
          .catch(error => {
            console.error("Error:", error);
            this.result = null;
            this.error = "查询失败，请稍后再试";
          });
    }
  }
}
</script>