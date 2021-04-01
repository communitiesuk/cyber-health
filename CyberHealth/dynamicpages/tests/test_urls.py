from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dynamicpages.views import start_page


class TestViews(SimpleTestCase):

    def test_start_page_url_resolves(self):
        url = reverse('dynamic-page')
        self.assertEquals(resolve(url).func, start_page)