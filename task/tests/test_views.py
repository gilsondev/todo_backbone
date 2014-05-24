# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class TasksTest(APITestCase):
    def test_list_tasks(self):
        """
        Should list all tasks
        """
        response = self.client.get(reverse('task_list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
