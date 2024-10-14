import os
import django

# 配置Django环境变量（将doctor_back.settings替换为你的实际项目路径）
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_back.settings')

# 初始化Django
django.setup()

from restapi.models import MedicalStore  # 导入模型
from django.db.models import Q


def search_database_console(query):
    if query:
        # 使用Q对象进行模糊查询，搜索`h`、`t`或`r`字段
        results = MedicalStore.objects.filter(
            Q(h__icontains=query) | Q(t__icontains=query) | Q(r__icontains=query)
        ).values('h', 't', 'r')

        if results:
            print(f"查询字符串: {query}")
            for result in results:
                print(f"h: {result['h']}, t: {result['t']}, r: {result['r']}")
        else:
            print(f"未找到与'{query}'匹配的结果。")
    else:
        print("查询字符串不能为空！")


if __name__ == "__main__":
    query = input("Test: 绕过views, 直接对models进行查询\n请输入查询字符串: ").strip()  # 从控制台获取用户输入的查询字符串
    search_database_console(query)
