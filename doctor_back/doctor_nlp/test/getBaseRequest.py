import json

import requests

# 定义 API 的 URL
url = 'http://127.0.0.1:8000/restapi/get-dataset/'  # 替换为实际的 URL

# 发送 POST 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析 JSON 响应
    data = response.json()
    print(json.dumps(data, indent=4, ensure_ascii=False))  # 格式化输出 JSON 数据
else:
    print(f"请求失败，状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
