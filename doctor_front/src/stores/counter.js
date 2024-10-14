// 导入一个方法 defineStore
import { defineStore } from 'pinia'
import {computed, ref} from 'vue'
import axios from "axios";
const API_URL = 'http://geek.itheima.net/v1_0/channels'

export const useCounterStore =defineStore('counter', () => {
    // 定义数据
    const count = ref(0)

    // 自增
    const increment = () => {
        count.value++
    }

    // getter
    const doubleCount = computed(() => count.value * 2)

    // action
    const list = ref([])
    const getList = async () => {
        const res = await axios.get(API_URL)
        list.value = res.data.data.channels
    }

    // 以对象的方式供组件使用
    return {
        count,
        doubleCount,
        increment,
        list,
        getList
    }
})