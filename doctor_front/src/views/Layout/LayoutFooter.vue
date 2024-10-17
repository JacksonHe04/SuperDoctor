<template>
  <footer class="app_footer">
    <!-- 联系我们 -->
    <div class="contact">
      <div class="container">
        <dl>
          <dt>关于我</dt>
          <dd>
            <a href="/src/assets/images/wechat_qrc.png" target="_blank">
              <i class="iconfont icon-wechat-fill"></i> 微信
            </a>
          </dd>
          <dd>
            <a href="https://yuque.com/jacksonhe" target="_blank">
              <i class="iconfont icon-yuque-fill"></i> 语雀
            </a>
          </dd>
        </dl>
        <dl>
          <dt>项目开源</dt>
          <dd>
            <a href="https://github.com/JacksonHe04" target="_blank">
              <i class="iconfont icon-github"></i>个人项目
            </a>
          </dd>
          <dd>
            <a href="https://github.com/JacksonHe04/SuperDoctor" target="_blank">
              <i class="iconfont icon-github"></i> GitHub仓库
            </a>
          </dd>
        </dl>
        <dl>
          <dt>联系我们</dt>
          <dd class="qrcode"><img src="@/assets/images/wechat_black.png"  alt="wx"/></dd>
          <dd class="download">
            <span>扫描二维码</span>
            <span>立即联系开发者</span>
            <a href="https://github.com/JacksonHe04/SuperDoctor" target="_blank">关于我们</a>
          </dd>
        </dl>
        <dl>
          <dt>服务热线</dt>
          <dd class="hotline">136-9566-3529 <small>周一至周日 8:00-18:00</small></dd>
        </dl>
      </div>
    </div>
    <!-- 其它 -->
    <div class="extra">
      <!-- 版权分隔线 -->
      <div class="seperator"></div>
      <div class="container">
        <!-- 版权信息 -->
        <div class="copyright">
          <p>
            CopyRight © 何锦诚 2024 All rights reserved.
          </p>
          <h2></h2>
          <p>
            东南大学人工智能学院《自然语言处理》课程作品
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped lang='scss'>
.app_footer {
  overflow: hidden;
  background-color: #f5f5f5;
  padding-top: 20px;

  .contact {
    background: #fff;

    .container {
      padding: 60px 0 40px 130px;
      display: flex;
    }

    dl {
      height: 190px;
      text-align: center;
      padding: 0 72px;
      border-right: 1px solid #f2f2f2;
      color: #999;

      &:first-child {
        padding-left: 0;
      }

      &:last-child {
        border-right: none;
        padding-right: 0;
      }
    }

    dt {
      line-height: 1;
      font-size: 18px;
      color: #999;
    }

    dd {
      margin: 36px 12px 0 0;
      float: left;
      width: 92px;
      height: 92px;
      padding-top: 10px;
      border: 1px solid #ededed;

      .iconfont {
        font-size: 36px;
        display: block;
        color: #666;
      }

      &:hover {
        .iconfont {
          color: $themeColor;
        }
      }

      &:last-child {
        margin-right: 0;
      }
    }

    .qrcode {
      width: 92px;
      height: 92px;
      padding: 7px;
      border: 1px solid #ededed;
    }

    .download {
      padding-top: 5px;
      font-size: 14px;
      width: auto;
      height: auto;
      border: none;

      span {
        display: block;
      }

      a {
        display: block;
        line-height: 1;
        padding: 10px 25px;
        margin-top: 5px;
        color: #999;
        border-radius: 2px;
        background-color: $themeTrans;
      }
    }

    .hotline {
      padding-top: 20px;
      font-size: 22px;
      color: #666;
      width: auto;
      height: auto;
      border: none;

      small {
        display: block;
        font-size: 15px;
        color: #999;
      }
    }
  }

  .extra {
    position: absolute;
    width: 100%;
  }

  .seperator {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: calc(50% + 20px); // 分隔线宽度稍大于容器
    height: 1px;
    background-color: #e0e0e0; // 灰色分隔线
  }

  .copyright {
    height: 130px;
    padding-top: 40px;
    text-align: center;
    color: #999;
    font-size: 15px;

    p {
      line-height: 1;
      margin-bottom: 20px;
    }

    a {
      color: #999;
      line-height: 1;
      padding: 0 10px;
      border-right: 1px solid #999;

      &:last-child {
        border-right: none;
      }
    }
  }
}
</style>
<script setup lang="ts">
</script>