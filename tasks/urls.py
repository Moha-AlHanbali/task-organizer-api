from django.http import request
from django.urls import path
from .views import ListTask, DetailTask, get_tasks


urlpatterns = [
    path('', ListTask.as_view(), name = 'ListTask'),
    path('<int:pk>/', DetailTask.as_view(), name = 'DetailTask'),
    path('get/', get_tasks, name = 'get_tasks')
]