# doctor_back/restapi/views.py
import json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TrainSet, ValSet, TestSet
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt  # 如果需要跨域请求


@api_view(['POST'])
def search_database(request):
    query = request.data.get('query', '').strip()  # 从POST请求体中获取数据

    if query:
        # 使用Q对象进行模糊查询，搜索`h`、`t`或`r`字段
        results = TrainSet.objects.filter(
            Q(h__icontains=query) | Q(t__icontains=query) | Q(r__icontains=query)
        ).values('h', 't', 'r')

        if results:
            print(f"用户输入了: {query}, Results: {list(results)}")  # 打印搜索结果
        else:
            print(f"未找到与'{query}'匹配的结果。")
        return Response({"results": list(results)})

    return Response({"results": []})


def get_train_set(request):
    if request.method == 'GET':
        # 获取所有 TrainSet 对象
        train_sets = TrainSet.objects.all()

        # 构建响应数据
        data = [
            {
                'auto_id': train_set.auto_id,
                'sentence': train_set.sentence,
                'h': train_set.h,
                't': train_set.t,
                'r': train_set.r
            }
            for train_set in train_sets
        ]

        # 返回 JSON 响应
        return JsonResponse(data, safe=False)

    # 如果请求方法不是 POST，返回 405 Method Not Allowed
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)
