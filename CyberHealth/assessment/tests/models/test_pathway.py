from django.test import TestCase
from assessment.models import Pathway, PathwayGroup


class PathwayTestCase(TestCase):
    def setUp(self):
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

    # Pathway model tests
    def test_pathway_has_long_name(self):
        self.assertEqual(self.pathway1.long_name,
                         "National Sector Network")

    def test_pathway_has_short_name(self):
        self.assertEqual(self.pathway1.short_name,
                         "NSN")

    def test_pathway_has_intro_text(self):
        self.assertEqual(self.pathway1.intro_text,
                         "This is a description for the NSN")

    def test_pathway_has_pathway_group(self):
        self.assertEqual(self.pathway1.pathway_group.name,
                         "Pathway group 1")

    def test_pathway_prepopulates_short_name(self):
        self.assertEqual(self.pathway2.short_name, "National Cyber Essentials")

    def test_pathway_prepopulates_slug(self):
        self.assertEqual(self.pathway1.slug, "nsn")

    def test_pathway_prepopulates_short_name_and_slug(self):
        self.assertEqual(self.pathway2.slug, "national-cyber-essentials")

    # Test if slug has been manually entered that it's in a slug format
    def test_pathway_formats_slug(self):
        self.assertEqual(self.pathway3.slug, "iso-29001")
