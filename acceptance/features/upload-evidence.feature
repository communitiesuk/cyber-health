Feature: Upload evidence to support my application

Scenario: User uploads a document
Given I can access the "assessment/test-upload" page
And I have a file available to upload
And I know how many files I have uploaded currently
When I click the "Choose file" button
And I select the file I want to upload
And I click the "Submit" button
Then I can see my file in the list of uploaded files