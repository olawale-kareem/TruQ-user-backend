from .test_setup import TestSetup
from ..models import User
from django.contrib import auth


class TestViews(TestSetup):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_with_data(self):
        res = self.client.post(
            self.register_url, self.user_data, format='json')
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.status_code, 201)

    def test_user_can_login_with_registered_data(self):
        self.client.post(
            self.register_url, self.user_data, format='json')
        res = self.client.post(
            self.login_url, self.user_data, format='json')
        user = auth.authenticate(
            email=self.user_data['email'], password=self.user_data['password'])
        self.assertNotEqual(user, None)
        self.assertEqual(user.is_authenticated, True)
        self.assertEqual(res.status_code, 200)

    def test_user_cannot_login_with_unregistered_data(self):
        res = self.client.post(
            self.login_url, self.user_data, format='json')
        self.assertEqual(res.status_code, 401)

    def test_unauthenticated_user_cannot_access_user_list(self):
        res = self.client.get(
            self.user_url, format='json')
        self.assertEqual(res.status_code, 401)

    def test_unathenticated_user_cannot_logout_all_user(self):

        self.client.post(
            self.register_url, self.user_data, format="json")
        self.client.post(
            self.login_url, self.user_data, format="json")
        res = self.client.get(
            self.logout_all_url, format="json")
        self.assertEqual(res.status_code, 401)
