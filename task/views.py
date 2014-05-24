# -*- coding: utf-8 -*-

from rest_framework import generics

from task.models import Task
from task.serializers import TaskSerializer


class TaskListView(generics.ListAPIView):
    model = Task
    serializer_class = TaskSerializer


class TaskNewView(generics.CreateAPIView):
    model = Task
    serializer_class = TaskSerializer
