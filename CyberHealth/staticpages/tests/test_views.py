from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from staticpages.views import start_page


class TestViews(SimpleTestCase):

    def test_start_page_url_resolves(self):
        url = reverse('static-page')
        self.assertEquals(resolve(url).func, start_page)


class DynamicPageViewTest(TestCase):
  def test_view_url_repsons_ok(self):
    response = self.client.get('/')
    self.assertEqual(200, response.status_code)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('static-page'))
    self.assertEqual(200, response.status_code)

  def test_dynamic_page_uses_intended_template(self):
    response = self.client.get(reverse('static-page'))
    self.assertTemplateUsed(response, 'staticpages/staticpage.html')

  def test_index_renders_intended_content(self):
    response = self.client.get(reverse('static-page'))
    content_as_text = response.content.decode("utf-8")
    self.assertIn('MHCLG STATIC content', content_as_text)
