from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    title = models.CharField(max_length=64)
    details = models.TextField()
    date = models.DateTimeField()
    complete = models.BooleanField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title