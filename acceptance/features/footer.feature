Feature: Static footer

Scenario: Footer contains link to privacy policy
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
Then I see a link to "/privacy-policy" in the footer

Scenario: Footer contains link to cookie policy
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
Then I see a link to "/cookie-policy" in the footer

Scenario: Footer contains link to Accessibility statement
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
Then I see a link to "/accessibility-statement" in the footer
