from django.test import TestCase
from django.urls import reverse
from assessment.models import Pathway, PathwayGroup


class OverviewViewTest(TestCase):

    def setUp(self):
        self.heading = "Hello"
        self.description = "Welcome to your overview page. Use this page to select which parts of the assessment you’d like to complete and to view your progress."
        self.pathwaygroup1 = PathwayGroup.objects.create(
            name="Pathway group 1",
            intro_text="This is pathway group 1",
            slug="pathway-group-1"
        )

        self.pathway1 = Pathway.objects.create(
            long_name="National Sector Network",
            short_name="NSN",
            intro_text="This is a description for the NSN",
            pathway_group=self.pathwaygroup1
        )

        self.pathway2 = Pathway.objects.create(
            long_name="National Cyber Essentials",
            intro_text="This is a description for the National Cyber Essentials",
            pathway_group=self.pathwaygroup1
        )

        self.pathway3 = Pathway.objects.create(
            long_name="ISO 29001",
            short_name="ISO 29001",
            intro_text="International standard on how to manage information security, with requirements for establishing, implementing, maintaining and continually improving an information security management system (ISMS).",
            slug="ISO 29001",
            pathway_group=self.pathwaygroup1

        )

        # self.question1 = Question.objects.create(
        #     question_text="Are users who install software or other active code on the Council’s systems without "
        #                   "permission subject to disciplinary action? "
        # )

        # self.choice1 = Choice.objects.create(
        #     choice_text="yes",
        #     question=self.question1
        # )
        # self.choice2 = Choice.objects.create(
        #     choice_text="no",
        #     question=self.question1
        # )
        # self.choice3 = Choice.objects.create(
        #     choice_text="other",
        #     question=self.question1
        # )

        # # Getting the id of question1
        # self.question1_id = Question.objects.last().id

    def test_overview_view_url_response_ok(self):
        response = self.client.get('/assessment/')
        self.assertEqual(200, response.status_code)

    def test_overview_view_url_by_name(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertEqual(200, response.status_code)

    def test_overview_page_uses_intended_template(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertTemplateUsed(
            response, 'assessment/assessment-overview.html', 'base.html')

    def test_overview_page_displays_heading(self):
        response = self.client.get('/assessment/')
        self.assertContains(
            response, "Your Council Cyber Health Overview")

    def test_overview_page_displays_page_description(self):
        response = self.client.get('/assessment/')
        self.assertContains(
            response, self.description)

    # def test_question_page_displays_question(self):
    #     response = self.client.get(f'/assessment/question/{self.question1_id}')
    #     self.assertContains(
    #         response, self.question1.question_text)

    # def test_question_page_displays_options_as_radio(self):
    #     response = self.client.get(f'/assessment/question/{self.question1_id}')
    #     self.assertContains(
    #         response, self.choice1.choice_text)
    #     self.assertContains(
    #         response, self.choice2.choice_text)
    #     self.assertContains(
    #         response, self.choice3.choice_text)

    # def test_question_page_displays_save_button(self):
    #     response = self.client.get(f'/assessment/question/{self.question1_id}')
    #     self.assertContains(
    #         response,
    #         '<button class="govuk-button" data-module="govuk-button" type="submit" value="Submit">Save</button>',
    #         html=True)

    # def test_question_page_displays_back_link(self):
    #     response = self.client.get(f'/assessment/question/{self.question1_id}')
    #     self.assertContains(
    #         response, '<a href="/assessment/" class="govuk-back-link">Back</a>', html=True)

    # def test_creation_of_answer_model_instance(self):
    #     # Post request should create an answer
    #     self.client.post(reverse('question', args=[self.question1_id]), data={
    #                      'choice': ['1']})

    #     # Retrieve this question just created from the POST request
    #     self.new_answer_id = Answer.objects.last().id
    #     self.new_answer = Answer.objects.get(pk=self.new_answer_id)

    #     # Check if answer has correct content
    #     self.assertEqual(self.new_answer.question.question_text,
    #                      self.question1.question_text)
    #     self.assertEqual(self.new_answer.choice.choice_text,
    #                      self.choice1.choice_text)
