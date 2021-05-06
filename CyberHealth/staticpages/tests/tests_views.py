from django.test import TestCase
from django.urls import reverse


class StaticPageViewTest(TestCase):
    def test_view_url_response_ok(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('static-page'))
        self.assertEqual(200, response.status_code)

    def test_static_page_uses_intended_template(self):
        response = self.client.get(reverse('static-page'))
        self.assertTemplateUsed(response, 'staticpages/index.html')

    def test_can_render_privacy_policy(self):
        response = self.client.get('/privacy-policy')
        self.assertTemplateUsed(response, 'staticpages/privacy-policy.html')
    
    def test_can_render_cookie_policy(self):
        response = self.client.get('/cookie-policy')
        self.assertTemplateUsed(response, 'staticpages/cookie-policy.html')
    
    def test_can_render_accessibility_statement(self):
        response = self.client.get('/accessibility-statement')
        self.assertTemplateUsed(response, 'staticpages/accessibility-statement.html')
