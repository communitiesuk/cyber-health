from django.test import TestCase
from assessment.models import Question, Answer

class AnswerTestCase(TestCase):
    def setUp(self):
        self.question1 = Question.objects.create(
            question_text="Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?"
        )

        self.answer1 = Answer.objects.create(
            question=self.question1,
            response=True
        )

    # Answer model tests
    def test_answer_has_question(self):
        self.assertEqual(self.answer1.question.question_text,
                         "Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?")

    def test_answer_has_response(self):
        self.assertEqual(self.answer1.response, True)
