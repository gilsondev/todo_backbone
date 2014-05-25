# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from task.models import Task


class TasksTest(APITestCase):
    def test_list_tasks(self):
        """
        Should list all tasks
        """
        response = self.client.get(reverse('todo_list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        """
        Should create a task
        """
        data = {'description': 'Task Test', 'status': 'incomplete'}
        response = self.client.post(reverse('task_new'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data['id'] = 1
        self.assertEqual(response.data, data)

    def test_update_task(self):
        """
        Should retrieve task and update it.
        """
        data = {'description': 'Task Test', 'status': 'incomplete'}
        task = Task.objects.create(**data)

        data_updated = {'description': 'Update Task', 'status': 'incomplete'}
        response = self.client.put(reverse('task_update',
                                           kwargs={'pk': task.pk}),
                                   data_updated,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('description'),
                            data_updated.get('description'))

    def test_task_completed(self):
        """
        Should retrieve task and define as completed
        """
        data = {'description': 'Task Test', 'status': 'incomplete'}
        task = Task.objects.create(**data)

        data_updated = {'description': data.get('description'),
                        'status': 'complete'}
        response = self.client.put(reverse('task_update',
                                           kwargs={'pk': task.pk}),
                                   data_updated,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status'),
                         data_updated.get('status'))

