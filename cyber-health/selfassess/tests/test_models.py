from django.test import TestCase
from selfassess.models import *

# Create your tests here.
class SectionTestCase(TestCase):
  def setUp(self):
    self.manage = Section.objects.create(
      name="Section 1: MANAGE security risk", 
      body="""This section covers the organisational structures, policies and processes necessary to understand, 
              assess and systematically manage security risks to English public sector organisations’ network and 
              information systems and essential services. The security control categories under this section cover:"""
              )
    self.protect = Section.objects.create(
      name = "Section 2: PROTECT against cyber-attack",
      body = "This section covers the requirement for proportionate security measures to be in place to protect English public sector organisations (and their essential services and systems) from cyber-attack. The security control categories under this section cover:"
    )

  def test_section_has_name(self):
    self.assertEqual("Section 1: MANAGE security risk", self.manage.name)
