<template>
  <div class="hero-section">
    <!-- 添加 canvas 作为背景 -->
    <canvas id="bubbleCanvas"></canvas>
    <div class="container">
      <h1 class="title">Super Doctor</h1>
      <p class="subtitle">Based on Natural Language Process</p>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeTitle',
  mounted() {
    this.initBubbles();
  },
  methods: {
    initBubbles() {
      const canvas = document.getElementById('bubbleCanvas');
      const ctx = canvas.getContext('2d');
      let bubbles = [];
      let width = canvas.width = window.innerWidth;
      let height = canvas.height = window.innerHeight;

      // 生成随机颜色的泡泡
      function randomColor() {
        return 'rgba(136,202,139,0.3)'; // 浅绿色泡泡
      }

      // 定义泡泡类
      class Bubble {
        constructor() {
          this.x = Math.random() * width;
          this.y = Math.random() * height;
          this.radius = Math.random() * 20 + 10; // 泡泡的大小
          this.speedX = Math.random() * 2 - 1;
          this.speedY = Math.random() * 1 - 0.5;
          this.color = randomColor();
        }

        update() {
          this.x += this.speedX;
          this.y += this.speedY;

          // 边界检测并反弹
          if (this.x > width + this.radius || this.x < -this.radius) {
            this.speedX = -this.speedX;
          }
          if (this.y > height + this.radius || this.y < -this.radius) {
            this.speedY = -this.speedY;
          }
        }

        draw() {
          ctx.beginPath();
          ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
          ctx.fillStyle = this.color;
          ctx.fill();
        }
      }

      // 初始化泡泡
      function initBubbles() {
        bubbles = [];
        for (let i = 0; i < 50; i++) { // 控制泡泡的数量
          bubbles.push(new Bubble());
        }
      }

      // 动画循环
      function animate() {
        ctx.clearRect(0, 0, width, height); // 清除之前的帧
        bubbles.forEach(bubble => {
          bubble.update();
          bubble.draw();
        });
        requestAnimationFrame(animate); // 不断调用动画
      }

      // 窗口大小变化时调整canvas大小
      window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
        initBubbles();
      });

      initBubbles();
      animate();
    }
  }
}
</script>

<style scoped>
.hero-section {
  position: relative;
  display: flex;
  justify-content: center;
  min-height: calc(100vh - 60px);
  background-color: #f5f5f5;
  overflow: hidden; /* 防止泡泡溢出 */
}

#bubbleCanvas {
  position: absolute;
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
  font-size: 4rem;
  color: #333;
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
