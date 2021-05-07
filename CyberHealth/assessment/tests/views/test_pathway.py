from django.test import TestCase

from assessment.models import Pathway, PathwayGroup


class PathwayViewTest(TestCase):

    def setUp(self):

        self.pathway_group = PathwayGroup.objects.create(
            name="Pathway group 1",
            intro_text="This is pathway group 1",
            slug="pathway-group-1"
        )

        self.pathway1 = Pathway.objects.create(
            long_name="National Sector Network",
            short_name="NSN",
            intro_text="This is a description for the NSN",
            pathway_group=self.pathway_group
        )

    def test_pathway_view_url_response_ok(self):
        response = self.client.get('/assessment/nsn')
        self.assertEqual(200, response.status_code)

    def test_pathway_page_uses_intended_template(self):
        response = self.client.get('/assessment/nsn')
        self.assertTemplateUsed(
            response, 'assessment/pathway.html', 'base.html')

    def test_pathway_page_displays_heading(self):
        response = self.client.get('/assessment/nsn')
        self.assertContains(
            response, "National Sector Network")

    def test_pathway_page_displays_intro_text(self):
        response = self.client.get('/assessment/nsn')
        self.assertContains(
            response, "This is a description for the NSN")
