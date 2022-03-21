from django.urls import reverse
from rest_framework.test import APITestCase
from faker import Faker


class TestSetup(APITestCase):

    def setUp(self):

        self.register_url = reverse('register-user')
        self.login_url = reverse('login-user')
        self.user_url = reverse('all-users')
        self.logout_url = reverse('logout-user')
        self.logout_all_url = reverse('logout-all-users')

        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email().split('@')[1],
        }

        return super().setUp()

    def tearDown(self):

        return super().tearDown()
