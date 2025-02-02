from django.test import TestCase
from django.core import mail
from django.urls import reverse


class TestHomePage(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')

    
    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def testContactPage_tempplate(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_contact_form(self):
        response = self.client.post('/contact/', {
            'name': 'test',
            'email': 'test@gmail.com',
            'message': 'test message',
            
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/contact/')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Message from test (test@gmail.com)')
        self.assertEqual(mail.outbox[0].body, 'test message')
        self.assertEqual(mail.outbox[0].from_email, 'studentinstitute2024@gmail.com')
        


    