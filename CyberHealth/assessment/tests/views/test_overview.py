from django.test import TestCase
from django.urls import reverse
from assessment.models import Pathway, PathwayGroup
from users.models import Organisation
from django.contrib.auth.models import User
from django.test import Client


class OverviewViewTest(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 'TestUser321'
        self.test_user = User.objects.create_user(username=self.username)
        self.test_user.set_password(self.password)

        self.any_organisation = Organisation.objects.get(pk=1)
        self.test_user.organisation_set.add(self.any_organisation)

        self.test_user.save()
        self.client = Client()
        self.client.login(username=self.username, password=self.password)

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
        response = self.client.get(reverse('assessment-overview'))
        self.assertEqual(200, response.status_code)

    def test_overview_view_url_by_name(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertEqual(200, response.status_code)

    def test_overview_page_uses_intended_template(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertTemplateUsed(
            response, 'assessment/assessment-overview.html', 'base.html')

    def test_overview_page_displays_heading(self):
        self.response = self.client.get(reverse('assessment-overview'))
        self.assertContains(
            self.response, "Your Council Cyber Health Overview")

    def test_overview_page_displays_page_description(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertContains(
            response, self.description)

    def test_overview_page_displays_pathway_group(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertContains(
            response, self.pathwaygroup1.name)
        self.assertContains(
            response, self.pathwaygroup1.intro_text)

    def test_overview_page_displays_pathway(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertContains(
            response, self.pathway1.short_name)
        self.assertContains(
            response, self.pathway1.intro_text)

    def test_overview_page_has_pathway_link(self):
        response = self.client.get(reverse('assessment-overview'))
        self.assertContains(
            response, f'href="{self.pathway1.slug}"')
