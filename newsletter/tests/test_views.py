from django.test import TestCase
from django.urls import reverse
from newsletter.models import NewsletterSubscriber

class NewsletterSubscriptionTest(TestCase):

    def test_newsletter_subscription_success(self):
        """Test if a user can successfully subscribe to the newsletter."""
        response = self.client.post(reverse('subscribe_newsletter'), {'email': 'testuser@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(NewsletterSubscriber.objects.filter(email='testuser@example.com').exists())

    def test_newsletter_duplicate_subscription(self):
        """Test if a duplicate subscription is prevented."""
        NewsletterSubscriber.objects.create(email='testuser@example.com')
        response = self.client.post(reverse('subscribe_newsletter'), {'email': 'testuser@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(NewsletterSubscriber.objects.filter(email='testuser@example.com').count(), 1)

    def test_newsletter_invalid_email(self):
        """Test if an invalid email is rejected."""
        response = self.client.post(reverse('subscribe_newsletter'), {'email': 'invalid-email'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(NewsletterSubscriber.objects.filter(email='invalid-email').exists())
