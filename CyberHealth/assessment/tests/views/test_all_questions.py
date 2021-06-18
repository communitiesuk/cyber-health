from django.test import TestCase
from django.urls import reverse
from users.models import Organisation
from django.contrib.auth.models import User
from django.test import Client


class AllQuestionsViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'TestUser321'
        self.test_user = User.objects.create_user(username=self.username)
        self.test_user.set_password(self.password)

        self.any_organisation = Organisation.objects.get(pk=1)
        self.test_user.organisation_set.add(self.any_organisation)

        self.test_user.save()
        self.client = Client()
        self.client.login(username=self.username, password=self.password)

    def test_assessment_index_view_url_response_ok(self):
        response = self.client.get(reverse('all-questions'))
        self.assertEqual(200, response.status_code)

    def test_assessment_index_view_url_by_name(self):
        response = self.client.get(reverse('all-questions'))
        self.assertEqual(200, response.status_code)

    def test_assessment_index_uses_intended_template(self):
        response = self.client.get(reverse('all-questions'))
        self.assertTemplateUsed(response, 'assessment/all-questions.html')
