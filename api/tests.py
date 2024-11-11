from django.test import TestCase
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class UserRoleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "testus", password = "Password123!")

        self.librarian = User.objects.create_user(username="librarian", password="Password123!")
        self.librarian_group, created = Group.objects.get_or_create(name="librarians")
        self.librarian.groups.add(self.librarian_group)

        self.admin_user = User.objects.create_superuser(username = "adminuser", password = "Password123!")

        self.user_token  = Token.objects.create(user=self.user)
        self.librarian_token  = Token.objects.create(user=self.librarian)
        self.admin_token  = Token.objects.create(user=self.admin_user)


        self.client = APIClient()

    def test_normal_user_cannot_add_books(self):
        # self.client.login(username = "testus", password= "Password123!")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        response = self.client.post('/api/books/', {'title':'Book Title', 'author': 'Sample', 'description': 'Sample Description','isbn': '1234567890123','pub_date': '2023-01-01'})
        self.assertEqual(response.status_code, 403)

    def test_librarian_can_add_books(self):
        # self.client.login(username = "librarian", password= "Password123!")
        self.client.credentials(HTTP_AUTHORIZATION = 'Token '+ self.librarian_token.key)
        response = self.client.post('/api/books/', {'title':'Book Title', 'author': 'Sample', 'description': 'Sample Description','isbn': '1234567890123','pub_date': '2023-01-01'})
        self.assertEqual(response.status_code, 201)

    def test_admin_can_add_books(self):
        # self.client.login(username = "adminuser", password= "Password123!")
        self.client.credentials(HTTP_AUTHORIZATION = 'Token '+ self.admin_token.key)
        response = self.client.post('/api/books/', {'title':'Book Title', 'author': 'Sample', 'description': 'Sample Description','isbn': '1234567890123','pub_date': '2023-01-01'})
        self.assertEqual(response.status_code, 201)

