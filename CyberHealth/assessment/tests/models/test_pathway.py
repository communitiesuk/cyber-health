from django.test import TestCase
from assessment.models import Pathway, PathwayGroup


class PathwayTestCase(TestCase):
    def setUp(self):
        self.pathwaygroup1 = PathwayGroup.objects.create(
            name="Other common standards",
            intro_text="Other standards that you can see how you map against based on your self assessment answers.",
            slug="other-common-standards"
        )

        self.pathway1 = Pathway.objects.create(
            long_name="Public Sector Network",
            short_name="PSN",
            intro_text="Walled garden’ approach that enables public sector organisations to work together and share resources in a secure, controlled environment.",
            pathway_group=self.pathwaygroup1
        )

        self.pathway2 = Pathway.objects.create(
            long_name="Cyber Essentials",
            intro_text="Government-backed scheme that helps organisations protect themselves against the threat of cyber attacks, providing basic controls organisations should have in place.",
            pathway_group=self.pathwaygroup1
        )

        self.pathway3 = Pathway.objects.create(
            long_name="ISO 27001",
            short_name="ISO 27001",
            intro_text="International standard on how to manage information security, with requirements for establishing, implementing, maintaining and continually improving an information security management system (ISMS).",
            slug="ISO 27001",
            pathway_group=self.pathwaygroup1

        )

    # Pathway model tests
    def test_pathway_has_long_name(self):
        self.assertEqual(self.pathway1.long_name,
                         "Public Sector Network")

    def test_pathway_has_short_name(self):
        self.assertEqual(self.pathway1.short_name,
                         "PSN")

    def test_pathway_has_intro_text(self):
        self.assertEqual(self.pathway1.intro_text,
                         "Walled garden’ approach that enables public sector organisations to work together and share resources in a secure, controlled environment.")

    def test_pathway_has_pathway_group(self):
        self.assertEqual(self.pathway1.pathway_group.name,
                         "Other common standards")

    def test_pathway_prepopulates_short_name(self):
        self.assertEqual(self.pathway2.short_name, "Cyber Essentials")

    def test_pathway_prepopulates_slug(self):
        self.assertEqual(self.pathway1.slug, "psn")

    def test_pathway_prepopulates_short_name_and_slug(self):
        self.assertEqual(self.pathway2.slug, "cyber-essentials")

    # Test if slug has been manually entered that's it in a slug format
    def test_pathway_formats_slug(self):
        self.assertEqual(self.pathway3.slug, "iso-27001")
