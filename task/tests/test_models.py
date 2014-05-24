# -*- coding: utf-8 -*-

from django.test import TestCase

from task.models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.fields = Task._meta.get_all_field_names()

    def test_description_field(self):
        """Should contain description field"""
        self.assertIn("description", self.fields)

    def test_status_field(self):
        """Should contain status field"""
        self.assertIn("status", self.fields)

    def test_status_choices(self):
        """Field status should contain choices"""
        field = Task._meta.get_field("status")
        self.assertIsInstance(field.choices, tuple)
        self.assertTupleEqual(field.choices, Task.STATUS_CHOICES)

