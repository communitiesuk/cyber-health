Feature: Register

Scenario: Sad path - Council already registered
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "register" link
And I use an email address using a domain that is a subsequent user related to a council in the CyberHealth framework
And I fill in the other details with valid information
And I click on the "Sign Up" button
Then I see a warning that I cannot login "There is already a user for your local council." 
