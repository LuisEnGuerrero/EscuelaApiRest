from datetime import date

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

# Create your tests here.
from tareas.models import Tarea


class TareasTestCase(APITestCase):

    def setUp(self) -> None:
        self.host = 'http://127.0.0.1:8000'
        self.user = User.objects.create_user(username='user', email='user@api.com', password='12345')

        response = self.client.post(
            f'{self.host}/api/token/',
            {'username': 'usertest', 'password': 'test'}
        )
        print(response.data)
        self.token = response.data['access']

        Tarea.objects.create(
            titulo='Tarea de prueba',
            descripción='Test para tareas',
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )

    def test_get_list(self):
        response = self.client.get(f'{self.host}/tareas/')

        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data['results']), 0)


    def test_create_tareas(self):
        tarea = {
            'titulo': 'Tarea de prueba post',
            'descripción': 'Test para tareas en post'
        }
        response = self.client.post(
            f'{self.host}/tareas/',
            data=tarea,
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, None)
        self.assertTrue(tarea.exists())

    def test_get_tareas(self):
        response = self.client.get(
            f'{self.host}/tareas/1/',
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.data, None)

    def test_edit_tareas(self):
        tareaEdit = {'titulo': 'titulo editado'}
        response = self.client.patch(
            f'{self.host}/tareas/1/',
            tareaEdit,
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, None)
        self.assertEqual(response.data['titulo'], tareaEdit['titulo'])
        self.assertNotEqual(response.data['id'], 1)

    def test_delete_tareas(self):
        response = self.client.delete(
            f'{self.host}/tareas/1/',
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )
        self.assertEqual(response.data, None)
        self.assertNotEqual(len(response.data['results']), 1)
