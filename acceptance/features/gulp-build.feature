Feature: Gulp builds CSS from source

Scenario: CSS file exists at build target
Given I am able to view a web page
When I visit the base URL
Then I see a header with the background color of "rgb(11, 12, 12)"