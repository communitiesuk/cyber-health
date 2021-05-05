from django.test import TestCase
from assessment.models import PathwayGroup


class PathwayGroupTestCase(TestCase):
    def setUp(self):
        self.pathwaygroup1 = PathwayGroup.objects.create(
            name="Pathway group 1",
            intro_text="This is pathway group 1",
        )
        self.pathwaygroup2 = PathwayGroup.objects.create(
            name="Pathway group 2",
            intro_text="This is pathway group 2",
            slug="PATHWAY GROUP 2"
        )

    # Pathway Group model tests
    def test_pathway_group_has_name(self):
        self.assertEqual(self.pathwaygroup1.name,
                         "Pathway group 1")

    def test_pathway_group_has_intro_text(self):
        self.assertEqual(self.pathwaygroup1.intro_text,
                         "This is pathway group 1")

    def test_pathway_group_prepopulates_slug(self):
        self.assertEqual(self.pathwaygroup1.slug, "pathway-group-1")

    # Test if slug has been manually entered that it's in a slug format
    def test_pathway_group_formats_slug(self):
        self.assertEqual(self.pathwaygroup2.slug, "pathway-group-2")
