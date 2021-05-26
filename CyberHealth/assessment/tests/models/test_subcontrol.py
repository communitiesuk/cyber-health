from django.test import TestCase
from assessment.models import Control, Pathway, PathwayGroup, SubControl


class SubControlTestCase(TestCase):
    def setUp(self):
        self.pathwaygroup1 = PathwayGroup.objects.create(
            name="Pathway group 1",
            intro_text="This is pathway group 1",
            slug="pathway-group-1"
        )

        self.nsn_pathway = Pathway.objects.create(
            long_name="National Sector Network",
            short_name="NSN",
            intro_text="This is a description for the NSN",
            pathway_group=self.pathwaygroup1
        )

        self.incident_response = Control.objects.create(
            title="Incident response plan",
            intro_text="You have a written incident response plan that defines the roles of personnel as well as phases on incident handling/management."
        )

        self.subcontrol_auto_slug = SubControl.objects.create(
            title = "Organisation has a detailed incident response plan",
            control = self.incident_response
        )
        
        self.subcontrol_custom_slug = SubControl.objects.create(
            title = "Organisation has a detailed incident response plan",
            control = self.incident_response,
            slug = 'some-custom-slug',
            sort_order = 9
        )

    def test_subcontrol_has_title(self):
        self.assertEqual(self.subcontrol_auto_slug.title,
                         "Organisation has a detailed incident response plan")


    def test_subcontrol_has_provided_slug(self):
        self.assertEqual(self.subcontrol_custom_slug.slug,
                         "some-custom-slug")

    def test_subcontrol_creates_slug_when_not_provided(self):
        self.assertEqual(self.subcontrol_auto_slug.slug,
                         "organisation-has-a-detailed-incident-response-plan")

    def test_subcontrol_belongs_to_single_control(self):      
      self.assertTrue(isinstance(self.subcontrol_auto_slug.control, Control))
