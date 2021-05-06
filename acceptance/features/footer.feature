Feature: Index page loads

Scenario: Footer contains link to privacy policy
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
Then I see a link to "/privacy-policy" in the footer