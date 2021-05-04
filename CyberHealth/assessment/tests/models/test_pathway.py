from django.test import TestCase
from assessment.models import *


class PathwayTestCase(TestCase):
    def setUp(self):
        self.pathway1 = Pathway.objects.create(
            long_name="Public Sector Network",
            short_name="PSN",
            intro_text="Walled garden’ approach that enables public sector organisations to work together and share resources in a secure, controlled environment."
        )

        self.pathway2 = Pathway.objects.create(
            long_name="Cyber Essentials",
            intro_text="Government-backed scheme that helps organisations protect themselves against the threat of cyber attacks, providing basic controls organisations should have in place."
        )

    # Pathway model tests
    def test_pathway_has_long_name(self):
        self.assertEqual(self.pathway1.long_name,
                         "Public Sector Network")

    def test_pathway_has_short_name(self):
        self.assertEqual(self.pathway1.short_name,
                         "PSN")

    def test_pathway_prepopulates_short_name(self):
        self.assertEqual(self.pathway2.short_name,
                         "Cyber Essentials")

    # def test_answer_has_choice(self):
    #     self.assertEqual(self.answer1.choice.choice_text, "yes")
