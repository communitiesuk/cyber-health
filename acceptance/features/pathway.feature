Feature: Pathway page loads

Scenario: Pathway page contains expected text
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework pathway page
Then I see the text "Public Sector Network"

Scenario: Pathway page renders controls
Given I am a Cyber Capable Person
When I visit the PSN pathway page
Then I see a control with id and title "1 Written incident response plan"