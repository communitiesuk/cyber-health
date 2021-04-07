from django.test import TestCase
from django.urls import reverse, resolve

class DynamicPageViewTest(TestCase):
  def test_view_url_repsons_ok(self):
    response = self.client.get('/dynamic/')
    self.assertEqual(200, response.status_code)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('dynamic-page'))
    self.assertEqual(200, response.status_code)

  def test_dynamic_page_uses_intended_template(self):
    response = self.client.get(reverse('dynamic-page'))
    self.assertTemplateUsed(response, 'dynamicpages/dynamicpage.html')

  def test_index_renders_intended_content(self):
    response = self.client.get(reverse('dynamic-page'))
    content_as_text = response.content.decode("utf-8")
    self.assertIn('MHCLG DYNAMIC content', content_as_text)
