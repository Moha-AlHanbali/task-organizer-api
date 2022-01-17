from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.core import serializers
from django.http import HttpResponse

from .serializers import TaskSerializer
from .models import Task
from .permissions import IsOwner

class ListTask(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(request.data, status=status.HTTP_201_CREATED)


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def get_tasks(request):
    auth_user = request.user
    if auth_user.is_authenticated:
        tasks = Task.objects.filter(user = auth_user)
        tasks_json = serializers.serialize('json', tasks)
        return HttpResponse(tasks_json, content_type='application/json')
    else:
        return HttpResponse(status = status.HTTP_403_FORBIDDEN)

