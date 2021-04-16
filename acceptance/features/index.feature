Feature: Index page loads

Scenario: Index page contains expected text
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
Then I see the text "Default page template"