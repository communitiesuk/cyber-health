from django.test import TestCase
from django.urls import reverse
from assessment.models import Question, Answer, PathwayGroup, Pathway


class QuestionViewTest(TestCase):

    def setUp(self):
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
