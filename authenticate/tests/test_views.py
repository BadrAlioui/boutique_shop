from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from authenticate.forms import SignUpForm, EditProfileForm


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.edit_profile_url = reverse('edit_profile')
        self.change_password_url = reverse('change_password')
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')

    def test_login_view_POST_valid(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_login_view_POST_invalid(self):
        response = self.client.post(self.login_url, {
            'username': 'invalid',
            'password': 'invalid'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/register.html')

    def test_register_view_POST_valid(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'email': 'user@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertTrue(User.objects.filter(email='user@example.com').exists())

    def test_edit_profile_view_POST_valid(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.edit_profile_url, {
            'username': 'testuser',
            'first_name': 'UpdatedFirstName',
            'last_name': 'UpdatedLastName',
            'email': 'updated@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedFirstName')
        self.assertEqual(self.user.last_name, 'UpdatedLastName')
        self.assertEqual(self.user.email, 'updated@example.com')

    def test_edit_profile_view_GET(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.edit_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/edit_profile.html')

    def test_edit_profile_view_POST_valid(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.edit_profile_url, {
            'username': 'testuser',
            'first_name': 'NewName',
            'last_name': 'LastName',
            'email': 'newname@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'NewName')
        self.assertEqual(self.user.email, 'newname@example.com')

    def test_change_password_view_GET(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.change_password_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/change_password.html')

    def test_change_password_view_POST_valid(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.change_password_url, {
            'old_password': 'testpass',
            'new_password1': 'newstrongpassword123',
            'new_password2': 'newstrongpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newstrongpassword123'))

    def test_change_password_view_POST_invalid(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.change_password_url, {
            'old_password': 'wrongpass',
            'new_password1': 'newstrongpassword123',
            'new_password2': 'newstrongpassword123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/change_password.html')

    def test_delete_account_view_GET(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('delete_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/delete_account.html')

    def test_delete_account_view_POST(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_my_profile_view_GET(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('my_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/my_profile.html')
