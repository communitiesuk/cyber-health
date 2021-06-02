from django.test import TestCase
from django.urls import reverse
from assessment.models import Question, Answer, PathwayGroup, Pathway
from django.contrib.auth.models import User
from django.test import Client


class QuestionViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'TestUser321'
        self.test_user = User.objects.create_user(username=self.username)
        self.test_user.set_password(self.password)
        self.test_user.save()
        self.client = Client()
        self.client.login(username=self.username, password=self.password)

        self.question1 = Question.objects.create(
            question_text="Are users who install software or other active code on the Council’s systems without "
                          "permission subject to disciplinary action? "
        )

        self.pathway_group = PathwayGroup.objects.create(
            name="Pathway group 1",
            intro_text="This is pathway group 1",
            slug="pathway-group-1"
        )

        self.pathway1 = Pathway.objects.create(
            long_name="National Sector Network",
            short_name="NSN",
            intro_text="This is a description for the NSN",
            pathway_group=self.pathway_group
        )

        # Getting the id of question1
        self.question1_id = Question.objects.last().id

    def test_question_page_displays_save_button(self):
        response = self.client.get(f'/assessment/nsn/question/{self.question1_id}')
        self.assertContains(
            response,
            '<button class="govuk-button" data-module="govuk-button" type="submit" value="Submit">Save</button>',
            html=True)

    def test_question_page_displays_back_link(self):
        response = self.client.get(f'/assessment/nsn/question/{self.question1_id}')
        self.assertContains(
            response, '<a href="/assessment/" class="govuk-back-link">Back</a>', html=True)
