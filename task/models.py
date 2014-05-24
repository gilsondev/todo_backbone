# -*- coding: utf-8 -*-

from django.db import models


class Task(models.Model):
    description = models.TextField()
    status = models.CharField(max_length=30)
