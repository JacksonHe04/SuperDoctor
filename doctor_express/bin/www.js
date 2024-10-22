// doctor_express/bin/www.js
/**
 * bin目录用于存放启动脚本。
 * www.js文件负责启动Express应用，配置服务器并监听指定端口。
 */

// 引入Express应用实例
const app = require('../app');
// 引入调试工具
const debug = require('debug')('doctor-express:server');
// 引入HTTP模块
const http = require('http');

/**
 * 将环境变量中的端口转换为标准化的端口值。
 * @param {string} val - 端口值或管道名称。
 * @returns {number|string|boolean} 标准化的端口值，字符串或false。
 */
const port = normalizePort(process.env.PORT || '3000');
app.set('port', port);

/**
 * 创建HTTP服务器。
 */
const server = http.createServer(app);

/**
 * 监听指定端口，适用于所有网络接口。
 */
server.listen(port);
server.on('error', onError);
server.on('listening', onListening);

/**
 * 将端口标准化为数字、字符串或false。
 * @param {string} val - 端口值或管道名称。
 * @returns {number|string|boolean} 标准化的端口值，字符串或false。
 */
function normalizePort(val) {
  const port = parseInt(val, 10);

  if (isNaN(port)) {
    // named pipe
    return val;
  }

  if (port >= 0) {
    // port number
    return port;
  }

  return false;
}

/**
 * HTTP服务器“错误”事件的事件监听器。
 * @param {Error} error - 错误对象。
 */
function onError(error) {
  if (error.syscall !== 'listen') {
    throw error;
  }

  const bind = typeof port === 'string'
    ? 'Pipe ' + port
    : 'Port ' + port;

  // 处理特定的监听错误，显示友好的错误信息
  switch (error.code) {
    case 'EACCES':
      console.error(bind + ' requires elevated privileges');
      process.exit(1);
      break;
    case 'EADDRINUSE':
      console.error(bind + ' is already in use');
      process.exit(1);
      break;
    default:
      throw error;
  }
}

/**
 * HTTP服务器“监听”事件的事件监听器。
 */
function onListening() {
  const addr = server.address();
  const bind = typeof addr === 'string'
    ? 'pipe ' + addr
    : 'port ' + addr.port;
  debug('Listening on ' + bind);
}
