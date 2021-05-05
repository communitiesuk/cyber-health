from django.test import TestCase
from assessment.models import PathwayGroup


class PathwayGroupTestCase(TestCase):
    def setUp(self):
        self.pathwaygroup1 = PathwayGroup.objects.create(
            name="Other common standards",
            intro_text="Other standards that you can see how you map against based on your self assessment answers.",
        )
        self.pathwaygroup2 = PathwayGroup.objects.create(
            name="Compliance demands",
            intro_text="The compliance requirements that you can achieve through this self assessment:",
            slug="Compliance demands"
        )

    # Pathway Group model tests
    def test_pathway_group_has_name(self):
        self.assertEqual(self.pathwaygroup1.name,
                         "Other common standards")

    def test_pathway_group_has_intro_text(self):
        self.assertEqual(self.pathwaygroup1.intro_text,
                         "Other standards that you can see how you map against based on your self assessment answers.")

    def test_pathway_group_prepopulates_slug(self):
        self.assertEqual(self.pathwaygroup1.slug, "other-common-standards")

    # Test if slug has been manually entered that's it in a slug format
    def test_pathway_group_formats_slug(self):
        self.assertEqual(self.pathwaygroup2.slug, "compliance-demands")
