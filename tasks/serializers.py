from dataclasses import field
from django.forms import models
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'details', 'date', 'complete', 'user')