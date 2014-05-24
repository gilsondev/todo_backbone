# -*- coding: utf-8 -*-

from rest_framework import generics

from task.models import Task


class TaskListView(generics.ListAPIView):
    model = Task
