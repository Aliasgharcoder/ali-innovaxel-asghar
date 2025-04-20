# shortener/test_shortener.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import ShortURL

class URLShortenerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.original_url = "https://www.google.com"
        self.short_url_obj = ShortURL.objects.create(
            original_url=self.original_url,
            short_code="GoOg13"
        )

    def test_create_short_url(self):
        response = self.client.post(reverse('shorten_url'), {
            'original_url': 'https://example.com/some-page'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('short_code', response.data)

    def test_redirect_to_original_url(self):
        response = self.client.get(f"/api/{self.short_url_obj.short_code}/", follow=True)
        self.assertEqual(response.redirect_chain[-1][0], self.original_url)

    def test_get_url_stats(self):
        response = self.client.get(f"/api/{self.short_url_obj.short_code}/stats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['original_url'], self.original_url)

    def test_update_url(self):
        new_url = "https://updated.com"
        response = self.client.put(
            f"/api/{self.short_url_obj.short_code}/update/",
            {"original_url": new_url},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["original_url"], new_url)

    def test_delete_url(self):
        response = self.client.delete(f"/api/{self.short_url_obj.short_code}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ShortURL.objects.filter(short_code="GoOg13").exists())
