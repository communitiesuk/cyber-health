from django.test import TestCase
from assessment.models import Question, Choice, Answer

class AnswerTestCase(TestCase):
    def setUp(self):
        self.question1 = Question.objects.create(
            question_text="Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?"
        )

        self.choice1 = Choice.objects.create(
            choice_text="yes",
            question=self.question1
        )

        self.answer1 = Answer.objects.create(
            question=self.question1,
            choice=self.choice1
        )

    # Answer model tests
    def test_answer_has_question(self):
        self.assertEqual(self.answer1.question.question_text,
                         "Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?")

    def test_answer_has_choice(self):
        self.assertEqual(self.answer1.choice.choice_text, "yes")
