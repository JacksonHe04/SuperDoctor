# 中文医疗关系分类系统

## 项目简介
中文医疗关系分类系统旨在从中文医疗文本中识别并分类不同类型的医疗关系，包括药物、症状、疾病和治疗方法等。通过训练模型，系统能够帮助用户快速获取医疗信息，提高医疗数据的利用效率。

## 功能概述

### 管理者用户功能
- **新增语句进行分类**：允许管理者上传新的医疗文本，系统自动进行实体关系识别和分类，并记录进数据库。
- **数据库管理**：管理者可以查看、编辑和删除存储的语句及其分类结果，并监控分类模型的表现。

### 普通用户功能
- **症状查询**：用户可输入症状或病症，系统返回相关的医疗信息。
- **治疗和药物推荐**：查询特定疾病时，系统提供与该疾病相关的治疗方案和药物建议。
- **实体关系展示**：清晰展示输入的症状或疾病与其他实体的关系。

## 技术栈
- **前端**：Vue 3 + Vite
- **后端**：Django
- **数据库**：MySQL

## 数据集
本项目使用的中文医疗关系数据集分为训练集、测试集和验证集，分别包含 7000、2000 和 1000 条数据。数据格式为 JSON Lines，示例如下：

```json
{
  	"id": 0, 
  	"sentence": "早期先天性梅毒多见于早产儿、低出生体重儿或小于胎龄儿...", 
  	"h": "先天性梅毒", 
  	"t": "脑膜炎症状", 
  	"r": "临床表现"
}
```

## 安装与运行

### 前端
1. 克隆项目：
   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project/frontend
   ```

2. 安装依赖：
   ```bash
   npm install
   ```

3. 启动开发服务器：
   ```bash
   npm run dev
   ```

### 后端
1. 克隆项目：
   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project/backend
   ```

2. 创建虚拟环境并安装依赖：
   ```bash
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. 运行 Django 服务器：
   ```bash
   python manage.py runserver
   ```

### 使用说明
- 确保在相应部分替换 `your_username` 和 `your_project`，并根据项目的实际情况调整文件路径和安装命令。
- 如果有其他的使用说明、贡献指南或许可证信息，请根据需要添加或修改。