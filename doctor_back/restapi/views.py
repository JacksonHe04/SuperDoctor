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
    query = request.data.get('query', '').strip()  # 从POST请求体中获取查询字符串
    dataset = request.data.get('dataset', 'train')  # 从POST请求体中获取用户选择的数据集，默认为train

    if query:
        # 根据选择的数据集选择模型
        if dataset == 'train':
            queryset = TrainSet.objects.filter(
                Q(h__icontains=query) | Q(t__icontains=query) | Q(r__icontains=query)
            )
        elif dataset == 'val':
            queryset = ValSet.objects.filter(
                Q(h__icontains=query) | Q(t__icontains=query) | Q(r__icontains=query)
            )
        elif dataset == 'test':
            queryset = TestSet.objects.filter(
                Q(h__icontains=query) | Q(t__icontains=query) | Q(r__icontains=query)
            )
        else:
            return Response({"results": []})  # 如果选择了未知的数据集，返回空结果

        # 获取查询结果并返回
        results = queryset.values('h', 't', 'r')
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


def get_val_set(request):
    if request.method == 'GET':
        # 获取所有 TrainSet 对象
        val_sets = ValSet.objects.all()

        # 构建响应数据
        data = [
            {
                'auto_id': val_set.auto_id,
                'sentence': val_set.sentence,
                'h': val_set.h,
                't': val_set.t,
                'r': val_set.r
            }
            for val_set in val_sets
        ]

        # 返回 JSON 响应
        return JsonResponse(data, safe=False)

    # 如果请求方法不是 POST，返回 405 Method Not Allowed
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)


def get_test_set(request):
    if request.method == 'GET':
        # 获取所有 TrainSet 对象
        test_sets = TestSet.objects.all()

        # 构建响应数据
        data = [
            {
                'auto_id': test_set.auto_id,
                'sentence': test_set.sentence,
                'h': test_set.h,
                't': test_set.t,
                'r': test_set.r
            }
            for test_set in test_sets
        ]

        # 返回 JSON 响应
        return JsonResponse(data, safe=False)

    # 如果请求方法不是 POST，返回 405 Method Not Allowed
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)


