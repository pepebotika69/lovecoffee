from rest_framework.test import APIClient

from common.tests.base_test import NewUserTestCase


class UserLoginTestCase(NewUserTestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_user_login(self):
        self.client = APIClient()
        res = self.client.post(
            '/admin/login/?next=/admin/',
            {
                'username': self.username,
                'password': self.password
            },
            format='json'
        )

        self.assertEqual(res.status_code, 200)

    def tearDown(self) -> None:
        self.client.logout()
        super().tearDown()
