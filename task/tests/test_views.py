# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class TasksTest(APITestCase):
    def test_list_tasks(self):
        """
        Should list all tasks
        """
        response = self.client.get(reverse('todo_list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        """
        Sould create a task
        """
        data = {'description': 'Task Test', 'status': 'incomplete'}
        response = self.client.post(reverse('task_new'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data['id'] = 1
        self.assertEqual(response.data, data)
