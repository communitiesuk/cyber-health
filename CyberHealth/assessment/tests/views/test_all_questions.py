from django.test import TestCase
from django.urls import reverse



class AllQuestionsViewTest(TestCase):
    def test_assessment_index_view_url_response_ok(self):
        response = self.client.get('/assessment/all-questions', follow=True)
        self.assertEqual(200, response.status_code)

    def test_assessment_index_view_url_by_name(self):
        response = self.client.get(reverse('all-questions'))
        self.assertEqual(200, response.status_code)

    def test_assessment_index_uses_intended_template(self):
        response = self.client.get(reverse('all-questions'))
        self.assertTemplateUsed(response, 'assessment/all-questions.html')