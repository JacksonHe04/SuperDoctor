# restapi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('query_symptom/', views.query_symptom, name='query_symptom'),
    # path('upload/', views.upload_medical_text, name='upload_medical_text'),
    # path('all_data/', views.get_all_data, name='all_data'),
    path('search/', views.search_database, name='search_database'),
    path('get-dataset/', views.get_train_set, name='get_dataset'),

]
