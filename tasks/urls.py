from django.urls import path
from .views import ListTask, DetailTask


urlpatterns = [
    path('', ListTask.as_view(), name = 'ListTask'),
    path('<int:pk>/', DetailTask.as_view(), name = 'DetailTask')
]