from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

c = Client()

EMAIL = "pabiadzinski@gmail.com"
EMAIL_LOGIN = "pabiadzinski+test@gmail.com"
EMAIL_ERROR = "3hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk@mail.com"
NAME_ERROR = "123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk123123213123hjkj12h3kjh12k3hk12h3kj213h1k23hjk"
NAME = "testuser"
PASSWORD = "foo123qQ"


class Test(TestCase):
    # def setUp(self):
    #     self.user = get_user_model().objects.create_user(email='test@test.test', name='test', password=PASSWORD)
    #     self.user.save()

    # def tearDown(self):
    #     self.user.delete()

    def test_create_user(self):
        user = User.objects.create_user(email=EMAIL, name=NAME, password=PASSWORD)
        self.assertEqual(user.email, EMAIL)
        self.assertEqual(user.name, NAME)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(name='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', name='', password="foo")

    def test_signup(self):
        response = c.post(path=reverse("signup"), data={
            'name': NAME,
            'email': EMAIL,
            'password1': 'foo123qq',
            'password2': 'foo123qq'
        }, follow=True)

        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(response.status_code, 200)

        try:
            user = User.objects.get(email=EMAIL)
        except User.DoesNotExist:
            user = None

        self.assertEqual(user.email, EMAIL)
        self.assertEqual(user.name, NAME)

    def test_login(self):
        user = User.objects.create_user(email=EMAIL_LOGIN, name=NAME, password=PASSWORD)

        self.assertTrue(user.is_active)

        response = self.client.post(path=reverse("signin"), data={'email': EMAIL_LOGIN, 'password': PASSWORD},
                                    follow=True)

        self.assertEqual(str(response.context['user'].email), EMAIL_LOGIN)
