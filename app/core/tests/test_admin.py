from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.clien=Client()
        self.admin_user=get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='xyz123@',
        )
        self.clien.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(
            email='user@gmail.com',
            password='password12',
            name='TestUser',
        )

    def test_users_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.clien.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    

