
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        payload={
            'email':'test@gmail.com',
            'password': 'dfgjhfhhjf32',
            'name': 'Create User',
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exist(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'fjkjgjg4474',
            'name': 'Email Exist'
        }

        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload={
            'email': 'test@gmail.com',
            'password': 'pas',
            'name': 'Too Short', 
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email = payload['email']).exists()
        self.assertFalse(user_exists)

