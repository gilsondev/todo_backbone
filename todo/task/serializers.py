# -*- coding: utf-8 -*-

from rest_framework import serializers

from todo.task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Task.STATUS_CHOICES)
    class Meta:
        model = Task
        fields = ("id", "description", "status",)
