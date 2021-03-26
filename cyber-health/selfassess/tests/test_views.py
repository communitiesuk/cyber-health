from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
  def test_view_url_repsons_ok(self):
    response = self.client.get('/self-assess')
    self.assertEqual(200, response.status_code)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('index'))
    self.assertEqual(200, response.status_code)

  def test_index_uses_index_template(self):
    response = self.client.get(reverse('index'))
    self.assertTemplateUsed(response, 'selfassess/index.html')
  
  def test_index_renders_hello_world(self):
    response = self.client.get(reverse('index'))
    self.assertEqual('<p>Hello, world!</p>', response.content.decode("utf-8"))
    


  
