# doctor_back/restapi/models.py
from django.db import models


class MedicalStore(models.Model):
    auto_id = models.AutoField(primary_key=True)  # 自增主键
    id = models.IntegerField(null=True, blank=True)  # 允许为空
    sentence = models.TextField(null=True, blank=True)  # 允许为空
    h = models.CharField(max_length=255, null=True, blank=True)  # 症状
    t = models.CharField(max_length=255, null=True, blank=True)  # 疾病
    r = models.CharField(max_length=255, null=True, blank=True)  # 临床表现

    class Meta:
        db_table = 'train'

        def __str__(self):
            return self.h
