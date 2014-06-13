# -*- coding: utf-8 -*-

from rest_framework import generics

from task.models import Task
from task.serializers import TaskSerializer


class TaskListView(generics.ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer


class TaskUpdateView(generics.RetrieveUpdateAPIView):
    model = Task
    serializer_class = TaskSerializer
