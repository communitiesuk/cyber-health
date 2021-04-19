from django.test import TestCase
from django.urls import reverse
from assessment.models import Question, Answer, Choice


class AssessmentIndexViewTest(TestCase):
    def test_assessment_index_view_url_response_ok(self):
        response = self.client.get('/assessment', follow=True)
        self.assertEqual(200, response.status_code)

    def test_assessment_index_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(200, response.status_code)

    def test_assessment_index_uses_intended_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'assessment/index.html')


class QuestionsViewTest(TestCase):

    def setUp(self):
        self.question1 = Question.objects.create(
            question_text="Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?"
        )
        self.choice1 = Choice.objects.create(
            choice_text="yes", 
            question=self.question1
                                             )
        self.choice2 = Choice.objects.create(
            choice_text="no",
            question=self.question1
        )
        self.choice3 = Choice.objects.create(
            choice_text="other",
            question=self.question1
        )

    def test_question_view_url_response_ok(self):
        response = self.client.get('/assessment/question/1')
        self.assertEqual(200, response.status_code)

    def test_question_view_url_by_name(self):
        response = self.client.get(reverse('question', args=[1]))
        self.assertEqual(200, response.status_code)

    def test_question_page_uses_intended_template(self):
        response = self.client.get(reverse('question', args=[1]))
        self.assertTemplateUsed(
            response, 'assessment/question.html', 'base.html')

    def test_question_page_displays_question_as_heading(self):
        response = self.client.get('/assessment/question/1')
        self.assertContains(
            response, '<h1 class="govuk-fieldset__heading">Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?</h1>', html=True)

    def test_question_page_displays_options_as_radio(self):
        response = self.client.get('/assessment/question/1')
        self.assertContains(
             response,'<div class="govuk-radios__item"><input type="radio" name="choice" class="govuk-radios__input" id="yes" value="1"><label class="govuk-label govuk-radios__label" for="yes">Yes</label></div>', html=True)
        self.assertContains(
             response,'<div class="govuk-radios__item"><input type="radio" name="choice" class="govuk-radios__input" id="no" value="2"><label class="govuk-label govuk-radios__label" for="no">No</label></div>', html=True)
        self.assertContains(
             response,'<div class="govuk-radios__item"><input type="radio" name="choice" class="govuk-radios__input" id="other" value="3"><label class="govuk-label govuk-radios__label" for="other">Other</label></div>', html=True)

    def test_question_page_displays_save_button(self):
        response = self.client.get('/assessment/question/1')
        self.assertContains(
            response, '<button class="govuk-button" data-module="govuk-button" type="submit" value="Submit">Save</button>', html=True)

    def test_question_page_displays_back_link(self):    
        response = self.client.get('/assessment/question/1')
        self.assertContains(
            response, '<a href="/assessment/" class="govuk-back-link">Back</a>', html=True)