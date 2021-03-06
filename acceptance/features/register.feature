Feature: Register

Scenario: Sad path - Council already registered
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Create an account" link
And I use an email address using a domain that is a subsequent user related to a council in the CyberHealth framework
And I fill in the other details with valid information
And I click on the "Continue" button
Then I see a warning that I cannot register "There is already a user for your local council." 

Scenario: Sad Path - Weak password
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Create an account" link
And I use an email address using a domain that is a subsequent user related to a council in the CyberHealth framework
And I provide a weak password
And I fill in the other details with valid information
And I click on the "Continue" button
Then I see a warning that I cannot register "This password is too short. It must contain at least 8 characters." 

Scenario: Sad path - Email address previously registered
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Create an account" link
And I provide an email address using a domain that was previously registered and password and click register
And I fill in the other details with valid information
And I click on the "Continue" button
Then I see a warning that I cannot register "There is already a user for your local council."

Scenario: Sad path - Email address is not associated to a council
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click on the "Create an account" link
And I use an email address not using a domain related to a council in the CyberHealth framework
And I fill in the other details with valid information
And I click the "Continue" button
Then I see a warning that I cannot be signed up "Must use a .gov.uk email address related to a council"

Scenario: Sad Path - Commonly used password
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Create an account" link
And I use an email address using a domain that is a first user related to a council in the CyberHealth framework
And I provide a commonly used password
And I fill in the other details with valid information
And I click on the "Continue" button
Then I see a warning that I cannot register "This is a commonly used password. Please create a more unique password."

Scenario: Happy path - Success within one session
Given I am a Cyber Capable Person
When I visit the Cyber Health Framework site
And I click the "Create an account" link
And I use an email address using a domain that is a first user related to a council in the CyberHealth framework
And I fill in the other details with valid information
And I click on the "Continue" button
And I see my email address appears in the page
And I am asked to use my email to show that I am a user with access to the council email account
And On the same browser I use that confirmation link and account is activated
And I click the "Login to your account" link
Then I can login and see the assessment council overview screen