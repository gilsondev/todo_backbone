# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase
from rest_framework import status


class TasksTest(APITestCase):
    def test_list_tasks(self):
        """
        Should list all tasks
        """
        response = self.client.get('/api/todos/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
