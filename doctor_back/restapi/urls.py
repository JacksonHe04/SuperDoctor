# restapi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('query_symptom/', views.query_symptom, name='query_symptom'),
    path('upload/', views.upload_medical_text, name='upload_medical_text'),
    path('all_data/', views.get_all_data, name='all_data'),

]
