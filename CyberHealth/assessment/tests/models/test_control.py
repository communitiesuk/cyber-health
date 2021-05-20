from django.test import TestCase
from assessment.models import Control, Pathway, PathwayGroup, SubControl


class ControlTestCase(TestCase):
    def setUp(self):
        self.pathwaygroup1 = PathwayGroup.objects.create(
            name="Pathway group 1",
            intro_text="This is pathway group 1",
            slug="pathway-group-1"
        )

        self.psn_pathway = Pathway.objects.create(
            long_name="National Sector Network",
            short_name="NSN",
            intro_text="This is a description for the NSN",
            pathway_group=self.pathwaygroup1
        )

        self.incident_response = Control.objects.create(
            title="Written incident response plan",
            intro_text="You have a written incident response plan that defines the roles of personnel as well as phases on incident handling/management."
        )

        self.security_event_reporting = Control.objects.create(
            title="Security event reporting",
            intro_text="Security events are reported through defined procedures known to staff.",
            slug="security-event-reporting",
        )

        self.firewall = Control.objects.create(
            title="Security event reporting",
            intro_text="Security events are reported through defined procedures known to staff.",
            slug="security-event-reporting",
        )
