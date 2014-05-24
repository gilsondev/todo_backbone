# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    # Task status
    INCOMPLETE = 'incomplete'
    COMPLETE = 'complete'

    STATUS_CHOICES = (
        (_(u"Incomplete"), INCOMPLETE),
        (_(u"Complete"), COMPLETE),
    )

    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'tasks'
