from django.test import TestCase
from django.urls import reverse


class DynamicPageViewTest(TestCase):
    def test_view_url_response_ok(self):
        response = self.client.get('/dynamic/')
        self.assertEqual(200, response.status_code)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('dynamic-page'))
        self.assertEqual(200, response.status_code)

    def test_dynamic_page_uses_intended_template(self):
        response = self.client.get(reverse('dynamic-page'))
        self.assertTemplateUsed(response, 'dynamicpages/dynamicpage.html')

