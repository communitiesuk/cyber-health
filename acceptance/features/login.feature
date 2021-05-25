Feature: Login

Scenario: Successful from start
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Start self-assessment" link
And I provide a valid username and password and click login
Then I reach the index page

# Scenario: Index page contains expected heading
# Given I am a Cyber Capable Person
# When I visit the Cyber Health Framework site
# Then I see a page with the heading "Assess your cyber health"