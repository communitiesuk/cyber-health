Feature: Index page loads

Scenario: Index page contains expected heading
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
Then I see a page with the heading "Assess your cyber health"

Scenario: Index page contains skip to main content link
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I hit the tab key
And I click the "Skip to main content" link
Then I see a page with the heading "Assess your cyber health"