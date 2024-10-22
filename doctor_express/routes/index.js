// doctor_express/routes/index.js
// 引入Express框架
const express = require('express');
// 创建一个路由对象
const router = express.Router();

/**
 * 处理GET请求到主页
 */
router.get('/', function(req, res, next) {
  // 渲染index模板，传递一个包含title属性的对象
  res.render('index', { title: 'Express' });
});

// 导出路由模块，使其他模块可以引用
module.exports = router;
