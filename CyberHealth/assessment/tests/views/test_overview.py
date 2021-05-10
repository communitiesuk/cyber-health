from django.test import TestCase
from django.urls import reverse
from assessment.models import Pathway, PathwayGroup


class OverviewViewTest(TestCase):

    def setUp(self):
        self.description = "Welcome to your overview page. Use this page to"
        " select which parts of the assessment you’d like to complete and to"
        " view your progress."
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
            intro_text="This is a description for National Cyber Essentials",
            pathway_group=self.pathwaygroup1
        )

        self.pathway3 = Pathway.objects.create(
            long_name="ISO 29001",
            short_name="ISO 29001",
            intro_text="""International standard on how to manage information
            security, with requirements for establishing, implementing,
            maintaining and continually improving an information security
            management system (ISMS).""",
            slug="ISO 29001",
            pathway_group=self.pathwaygroup1

        )

    def test_overview_view_url_response_ok(self):
        response = self.client.get('/assessment/')
        self.assertEqual(200, response.status_code)

    def test_overview_view_url_by_name(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertEqual(200, response.status_code)

    def test_overview_page_uses_intended_template(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertTemplateUsed(
            response, 'assessment/assessment-overview.html', 'base.html')

    def test_overview_page_displays_heading(self):
        response = self.client.get('/assessment/')
        self.assertContains(
            response, "Your Council Cyber Health Overview")

    def test_overview_page_displays_page_description(self):
        response = self.client.get('/assessment/')
        self.assertContains(
            response, self.description)

    def test_overview_page_displays_pathway_group(self):
        response = self.client.get('/assessment/')
        self.assertContains(
            response, self.pathwaygroup1.name)
        self.assertContains(
            response, self.pathwaygroup1.intro_text)

    def test_overview_page_displays_pathway(self):
        response = self.client.get('/assessment/')
        self.assertContains(
            response, self.pathway1.short_name)
        self.assertContains(
            response, self.pathway1.intro_text)
    
    def test_overview_page_has_pathway_link(self):
        response = self.client.get('/assessment/')
        self.assertContains(
            response, f'href="{self.pathway1.slug}"')
