from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
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
        sample_emails=[
            ['TEST@GMAIL.COM', 'test@gmail.com'],
            ['Test@gmail.com', 'test@gmail.com'],
            ['Test@Gmail.Com', 'test@gmail.com'],
            ['Test@gmail.com', 'test@gmail.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, password='fggjugj45')
            self.assertEqual(user.email, expected)