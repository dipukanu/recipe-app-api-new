from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        email = 'test@gmail.com'
        password = 'xyz1234@'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@gmail.com', 'test1@gmail.com'],
            ['Test2@gmail.com', 'Test2@gmail.com'],
            ['TEST3@gmail.com', 'TEST3@gmail.com'],
            ['test4@gmail.COM', 'test4@gmail.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sdhbfdhbhubd')

    def test_create_superuser(self):
        email = 'test@gmail.com'
        user = get_user_model().objects.create_superuser(email, 'dfhfffhdbfh12')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

