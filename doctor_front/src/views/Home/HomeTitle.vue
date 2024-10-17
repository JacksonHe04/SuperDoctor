<template>
  <div class="hero-section">
    <!-- 添加 canvas 作为背景 -->
    <canvas id="bubbleCanvas"></canvas>
    <div class="container">
      <h1 class="title">Super Doctor</h1>
      <p class="subtitle">基于自然语言处理的中文医疗关系系统</p>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeTitle",
  mounted() {
    this.initBubbles();
  },

  methods: {
    initBubbles() {
      // 初始化泡泡的方法
      const canvas = document.getElementById("bubbleCanvas"); // 获取canvas元素
      const ctx = canvas.getContext("2d"); // 获取2D渲染上下文
      let bubbles = []; // 存储泡泡数组
      let width = (canvas.width = window.innerWidth); // 设置canvas宽度为窗口宽度
      let height = (canvas.height = window.innerHeight); // 设置canvas高度为窗口高度

      // 生成随机颜色的泡泡
      function randomColor() {
        return "rgba(136,202,139,0.3)"; // 返回固定浅绿色，实际应用中可以生成随机颜色
      }

      // 定义泡泡类
      class Bubble {
        constructor() {
          // 构造函数初始化泡泡位置、大小和速度
          this.x = Math.random() * width; // 随机x坐标
          this.y = Math.random() * height; // 随机y坐标
          this.radius = Math.random() * 20 + 10; // 随机半径
          this.speedX = Math.random() * 2 - 1; // 随机x方向速度
          this.speedY = Math.random() * 1 - 0.5; // 随机y方向速度
          this.color = randomColor(); // 设置泡泡颜色
        }

        update() {
          // 更新泡泡的位置
          this.x += this.speedX; // 移动x坐标
          this.y += this.speedY; // 移动y坐标

          // 边界检测并反弹
          if (this.x > width + this.radius || this.x < -this.radius) {
            this.speedX = -this.speedX; // 反弹x方向速度
          }
          if (this.y > height + this.radius || this.y < -this.radius) {
            this.speedY = -this.speedY; // 反弹y方向速度
          }
        }

        draw() {
          // 绘制泡泡
          ctx.beginPath(); // 开始路径
          ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2); // 绘制圆形
          ctx.fillStyle = this.color; // 设置填充颜色
          ctx.fill(); // 填充圆形
        }
      }

      // 初始化泡泡
      function initBubbles() {
        // 创建泡泡数组
        bubbles = []; // 清空泡泡数组
        for (let i = 0; i < 50; i++) {
          // 控制创建泡泡的数量
          bubbles.push(new Bubble()); // 创建并添加泡泡到数组
        }
      }

      // 动画循环
      function animate() {
        // 始终保持canvas的宽高与窗口一致
        // canvas.width = window.innerWidth;
        // canvas.height = window.innerHeight;
        // width = canvas.width;
        // height = canvas.height;

        // 动画绘制逻辑
        ctx.clearRect(0, 0, width, height); // 清除画布
        bubbles.forEach((bubble) => {
          // 对每个泡泡进行更新和绘制
          bubble.update(); // 更新泡泡位置
          bubble.draw(); // 绘制泡泡
        });
        requestAnimationFrame(animate); // 请求下一帧动画
      }

      // 窗口大小变化时调整canvas大小
      window.addEventListener("resize", () => {
        // 监听窗口大小变化
        width = canvas.width = window.innerWidth; // 调整canvas宽度
        height = canvas.height = window.innerHeight; // 调整canvas高度
        initBubbles(); // 重新初始化泡泡
      });

      initBubbles(); // 初始化泡泡
      animate(); // 启动动画
    },
  },
};
</script>

<style scoped lang="scss">
.hero-section {
  position: relative;
  display: flex;
  justify-content: center;
  min-height: calc(100vh - 60px);
  background-color: #f5f5f5;
  overflow: hidden; /* 防止泡泡溢出 */
}

#bubbleCanvas {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 0;
  width: 100%;
  height: 100%;
  pointer-events: none; /* 使泡泡不可点击 */
}

.container {
  position: relative;
  z-index: 1; /* 确保文本内容在泡泡之上 */
  text-align: center;
  margin-top: 120px;
}

.title {
  font-size: 4.4rem;
  color: $themeColor;
  margin-bottom: 0.5em;
  font-weight: bold;
}


.subtitle {
  font-size: 1.5rem;
  color: $greyColor2;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .title {
    font-size: 3rem;
  }

  .subtitle {
    font-size: 1.2rem;
  }
}
</style>
