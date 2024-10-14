import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './assets/main.css'
import './mock'
import router from './router'

// 引入初始化样式文件
import '@/styles/common.scss'

// 引入懒加载指令插件并且注册
// import { lazyPlugin } from '@/directives'
// 引入全局组件插件
// import { componentPlugin } from '@/components'

// 导入CreatePinia
import { createPinia } from 'pinia'

// 执行创建Pinia实例
// const pinia = createPinia()

// 挂载pinia实例到app中
// createApp(App).use(pinia).mount('#app')

import { getList } from '@/apis/testAPI.js';
getList().then(res => {
  console.log(res);
})

const app = createApp(App)
app.use(router)

// app.use(ElementPlus)
app.mount('#app')