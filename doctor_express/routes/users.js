// doctor_express/routes/users.js
const express = require('express');
const router = express.Router();

/**
 * GET方法处理用户列表请求.
 * 
 * 当发送GET请求到根路径('/')时,此函数被调用.
 * 它的作用是响应客户端请求,返回一个资源.
 */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
