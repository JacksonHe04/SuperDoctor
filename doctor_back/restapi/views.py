# doctor_back/restapi/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicalData
from django.db.models import Q


# 假设的模拟数据
MOCK_MEDICAL_DATA = [
    {
        "symptom": "头痛",
        "diagnosis": "偏头痛",
        "treatment": "休息，服用布洛芬",
        "medication": "布洛芬"
    },
    {
        "symptom": "咳嗽",
        "diagnosis": "普通感冒",
        "treatment": "多喝水，休息，服用止咳药",
        "medication": "右美沙芬"
    },
    {
        "symptom": "发烧",
        "diagnosis": "流感",
        "treatment": "卧床休息，服用退烧药",
        "medication": "对乙酰氨基酚"
    }
]

@api_view(['POST'])
def query_symptom(request):
    symptom = request.data.get('symptom', '').strip()
    if not symptom:
        return Response({"error": "No symptom provided"}, status=400)

    # 模拟查询，查找与输入症状相匹配的条目
    results = [data for data in MOCK_MEDICAL_DATA if symptom in data['symptom']]

    if results:
        return Response(results)  # 返回所有匹配的结果
    else:
        return Response({"message": "No related medical information found."}, status=404)


# 获取所有医疗数据的视图
@api_view(['GET'])
def get_all_data(request):
    return Response(MOCK_MEDICAL_DATA)


@api_view(['POST'])
def upload_medical_text(request):
    file = request.FILES.get('file')
    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    # 文件内容处理示例（假设每行是一个句子）
    for line in file:
        sentence = line.decode('utf-8').strip()
        # 实体关系识别逻辑
        # ...

        # 保存到数据库
        MedicalData.objects.create(sentence=sentence)  # 添加分类后的数据

    return Response({"message": "Upload and classification successful"})