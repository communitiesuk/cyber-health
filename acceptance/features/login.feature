Feature: Login

Scenario: Successful from start
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Start self-assessment" link
And I provide a valid username and password and click login
Then I reach the index page

Scenario: Successful from start and logout
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Start self-assessment" link
And I provide a valid username and password and click login
And I reach the index page
And I click the "logout" link
Then I reach the logged out page
And I see a message "You have signed out"
And I click the "Return to login" link
Then I reach the login page

Scenario: Successfully login to access deep content
Given I am a Cyber Capable Person
When I visit a page which requires a login
And I provide a valid username and password and click login
Then I reach the desired page

Scenario: wrong password or username combination
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Start self-assessment" link
And I provide a combination of valid username and an invalid password and click login
Then I see the login page
And I see a message explaining that the credentials provided were incorrect

Scenario: unknown username with password combination
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Start self-assessment" link
And I provide a combination of an unknown username and any password
Then I see the login page
And I see a message explaining that the credentials provided were incorrect
