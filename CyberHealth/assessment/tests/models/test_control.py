from django.test import TestCase
from assessment.models import Control, Pathway, PathwayGroup, SubControl


class ControlTestCase(TestCase):
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

        self.nce_pathway = Pathway.objects.create(
            long_name="National Cyber Essentials",
            intro_text="This is a description for the National Cyber Essentials",
            pathway_group=self.pathwaygroup1
        )

        self.incident_response = Control.objects.create(
            title="Incident response plan",
            intro_text="You have a written incident response plan that defines the roles of personnel as well as phases on incident handling/management."
        )

        self.security_event_reporting = Control.objects.create(
            title="Security event reporting process",
            intro_text="Security events are reported through defined procedures known to staff.",
            slug="some-custom-slug",
        )

        self.firewall = Control.objects.create(
            title="Firewall in place",
            intro_text="Your organisation has a firewall in place that prevents."
        )

    def test_control_has_title(self):
        self.assertEqual(self.incident_response.title,
                         "Incident response plan")

    def test_control_has_intro_text(self):
        self.assertEqual(self.incident_response.intro_text,
                         "You have a written incident response plan that defines the roles of personnel as well as phases on incident handling/management.")

    def test_control_has_provided_slug(self):
        self.assertEqual(self.security_event_reporting.slug,
                         "some-custom-slug")

    def test_control_creates_slug_when_not_provided(self):
        self.assertEqual(self.incident_response.slug,
                         "incident-response-plan")

    def test_control_can_be_added_to_pathway(self):
        # assert pathway has no controls
        self.assertEqual(self.nsn_pathway.controls.count(), 0)
        # add control to pathway
        self.nsn_pathway.controls.add(self.incident_response)
        # assert pathway has one control
        self.assertEqual(self.nsn_pathway.controls.count(), 1)

    def test_control_can_belong_to_multiple_pathways(self):
        # add control to two pathways
        self.nsn_pathway.controls.add(self.incident_response)
        self.nce_pathway.controls.add(self.incident_response)
        # assert each pathway has one control
        self.assertEqual(self.nsn_pathway.controls.count(), 1)
        self.assertEqual(self.nce_pathway.controls.count(), 1)
        # assert control belongs to two pathways
        self.assertEqual(self.incident_response.pathway_set.count(), 2)

