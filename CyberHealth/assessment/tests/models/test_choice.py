from django.test import TestCase
from assessment.models import Question, Choice

class ChoiceTestCase(TestCase):
    def setUp(self):
        self.question1 = Question.objects.create(
            question_text="Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?"
        )

        self.choice1 = Choice.objects.create(
            choice_text="yes",
            question=self.question1
        )

    # Choice model tests
    def test_choice_has_text(self):
        self.assertEqual(self.choice1.choice_text, "yes")

    def test_choice_has_question(self):
        self.assertEqual(self.choice1.question.question_text,
                         "Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?")
