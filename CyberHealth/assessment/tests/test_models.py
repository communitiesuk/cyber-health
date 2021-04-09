from django.test import TestCase
from assessment.models import Question, Choice, Answer


class QuestionTestCase(TestCase):
    def setUp(self):
        self.question1 = Question.objects.create(
            question_text="Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?"
        )

        self.choice1 = Choice.objects.create(
            choice_text="yes",
            question_id=self.question1
        )

        self.answer1 = Answer.objects.create(
            question_id=self.question1,
            choice_id=self.choice1
        )

    # Question model tests
    def test_question_has_text(self):
        self.assertEqual(self.question1.question_text,
                         "Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?")

    # Choice model tests
    def test_choice_has_text(self):
        self.assertEqual(self.choice1.choice_text, "yes")

    def test_choice_has_question(self):
        self.assertEqual(self.choice1.question_id.question_text,
                         "Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?")

    # Answer model tests
    def test_answer_has_question(self):
        self.assertEqual(self.answer1.question_id.question_text, "Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?")

    def test_answer_has_choice(self):
        self.assertEqual(self.answer1.choice_id.choice_text, "yes")    