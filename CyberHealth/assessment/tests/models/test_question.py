from django.test import TestCase
from assessment.models import Question


class QuestionTestCase(TestCase):
    def setUp(self):
        self.question1 = Question.objects.create(
            question_text="Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?"
        )

    # Question model tests
    def test_question_has_text(self):
        self.assertEqual(self.question1.question_text,
                         "Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?")