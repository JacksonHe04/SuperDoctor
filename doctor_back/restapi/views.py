# doctor_back/restapi/views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicalStore
from django.db.models import Q


@api_view(['POST'])
def search_database(request):
    query = request.data.get('query', '').strip()  # 从POST请求体中获取数据

    if query:
        # 使用Q对象进行模糊查询，搜索`h`、`t`或`r`字段
        results = MedicalStore.objects.filter(
            Q(h__icontains=query) | Q(t__icontains=query) | Q(r__icontains=query)
        ).values('h', 't', 'r')

        if results:
            print(f"用户输入了: {query}, Results: {list(results)}")  # 打印搜索结果
        else:
            print(f"未找到与'{query}'匹配的结果。")
        return Response({"results": list(results)})

    return Response({"results": []})
