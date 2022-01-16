from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task
from .permissions import IsOwnerOrReadOnly


class ListTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer