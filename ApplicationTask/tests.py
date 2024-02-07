from collections import OrderedDict

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task, Category
from .views import TaskSerializer, CategorySerializer
from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


class CategoryModelTests(APITestCase):
    """Category model tests CRUD"""
    def setUp(self):
        factory = APIRequestFactory()
        request = factory.get('/')

        serializer_context = {
            'request': Request(request),
        }

        self.url = 'http://127.0.0.1:8000/apiCategories/'
        self.data = {'name': 'test'}
        self.instance = Category.objects.create(**self.data)
        self.serializer = CategorySerializer(instance=self.instance, context=serializer_context)
        self.valid_payload = {'name': 'test'}
        User.objects.create_user(username='testuser', password='12345')

    def test_undefined_user_create_сategory_model(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_сategory_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_undefined_user_retrieve_сategory_model(self):
        response = self.client.get(f'{self.url}{self.instance.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer.data)

    def test_retrieve_сategory_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(f'{self.url}{self.instance.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer.data)

    def test_undefined_user_update_сategory_model(self):
        response = self.client.put(f'{self.url}{self.instance.pk}/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_сategory_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.put(f'{self.url}{self.instance.pk}/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.name, self.valid_payload['name'])

    def test_undefined_user_partial_update_сategory_model(self):
        response = self.client.patch(f'{self.url}{self.instance.pk}/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update_сategory_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.patch(f'{self.url}{self.instance.pk}/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.name, self.valid_payload['name'])

    def test_delete_сategory_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.delete(f'{self.url}{self.instance.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_undefined_user_delete_сategory_model(self):
        response = self.client.delete(f'{self.url}{self.instance.pk}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TaskModelTests(APITestCase):
    """Task model tests CRUD"""
    def setUp(self):
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        self.url = 'http://127.0.0.1:8000/apiTasks/'

        self.data = {
            'url': 'http://testserver/apiTasks/1/',
             'category': OrderedDict([('url', 'http://testserver/apiCategories/1/'), ('name', 'Test')]),
             'title': '11',
             'description': '11',
             'completed': 'False'
        }
        self.creation_data = {
             'title': '11',
             'description': '11',
             'completed': 'False'
        }

        category = Category.objects.create(name='Test')
        self.instance = Task.objects.create(category=category, **self.creation_data)
        self.serializer = TaskSerializer(instance=self.instance, context=serializer_context)
        self.valid_payload = {
            "title": "11",
            "description": "11",
            "completed": 'false'
        }
        User.objects.create_user(username='testuser', password='12345')

    def test_undefined_user_create_task_model(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_undefined_user_retrieve_task_model(self):
        response = self.client.get(f'{self.url}{self.instance.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer.data)

    def test_retrieve_task_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(f'{self.url}{self.instance.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer.data)

    def test_undefined_user_update_task_model(self):
        response = self.client.put(f'{self.url}{self.instance.pk}/', self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_task_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.put(f'{self.url}{self.instance.pk}/', self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.title, self.valid_payload['title'])

    def test_undefined_user_partial_update_task_model(self):
        response = self.client.patch(f'{self.url}{self.instance.pk}/', self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update_task_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.patch(f'{self.url}{self.instance.pk}/', self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.title, self.valid_payload['title'])

    def test_delete_task_model(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.delete(f'{self.url}{self.instance.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_undefined_user_delete_task_model(self):
        response = self.client.delete(f'{self.url}{self.instance.pk}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


