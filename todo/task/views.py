# -*- coding: utf-8 -*-

from rest_framework import generics

from todo.task.models import Task
from todo.task.serializers import TaskSerializer


class TaskListView(generics.ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer


class TaskUpdateView(generics.RetrieveUpdateAPIView):
    model = Task
    serializer_class = TaskSerializer
