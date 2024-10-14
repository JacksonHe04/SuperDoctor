// axios基础的封装
import axios from 'axios'

const httpInstance = axios.create(
    {
        baseURL: 'https://pcapi-xiaotuxian-front-devtest.itheima.net',
        timeout: 5000
    }
)

// 添加请求拦截器
httpInstance.interceptors.request.use(config => {
    return config
}, e => Promise.reject(e))

// 添加响应拦截器
httpInstance.interceptors.response.use(res => res.data, e => Promise.reject(e))

export default httpInstance