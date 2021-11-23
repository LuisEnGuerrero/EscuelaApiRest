from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase

from instituciones.models import Institucion


class InstitucionesTestCase(APITestCase):

    def setUp(self) -> None:
        self.host = 'http://127.0.0.1:8000'
        self.user = User.objects.create_user(username='user', email='user@api.com', password='12345')

        response = self.client.post(f'{self.host}/api/token/', {'username': 'user', 'password': '12345'})

        self.token = response.data['access']

        Institucion.objects.create(
            nombres='test',
            ciudad='Bogotá',
            pais='Colombia'
        )

    def test_get_list(self):
        response = self.client.get(f'{self.host}/instituciones/', HTTP_AUTHORIZATIONS=f'Bearer {self.token}')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data['results']), 0)

    def test_create_institucion(self):
        institucion = {
            "nombres": "institucion test",
            "direccion": "direccion test",
            "ciudad": "ciudad test",
            "pais": "pais test",
            "telefono": "0000000000"
        }
        response = self.client.post(
            f'{self.host}/instituciones/',
            data=institucion,
            HTTP_AUTHORIZATIONS=f'Bearer {self.token}'
            )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, None)
        self.assertTrue(institucion.exists())

