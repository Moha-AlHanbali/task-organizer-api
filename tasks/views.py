from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.core import serializers
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json

from .serializers import TaskSerializer
from .models import Task
from accounts.models import CustomUser
from .permissions import IsOwner

class ListTask(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
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

@csrf_exempt
def get_tasks(request):
    body = json.loads(request.body.decode('utf-8'))
    auth_user = CustomUser.objects.filter(pk=body['userID'])[0]
    if auth_user.is_authenticated:
        tasks = Task.objects.filter(user = auth_user)
        tasks_json = serializers.serialize('json', tasks)
        tasks_object = json.loads(tasks_json)
        res = {}

        for task in tasks_object:
            res.update({task['pk']:task['fields']})

        return JsonResponse(res, status = status.HTTP_200_OK)
    else:
        return HttpResponse(status = status.HTTP_403_FORBIDDEN)

