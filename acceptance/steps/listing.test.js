const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/listing.feature');

JestCucumber.defineFeature(feature, test => {
    test('Listing page contains expected text', ({ given, when, then }) => {
        let driver;

        given('I am a Cyber Capable Person', () => {
            driver = new FirefoxDriver();
        });

        when('I visit the Cyber Health Framework listing page', async() => {
            await driver.visitPage('assessment')
        });

        then(/I see the text \"(.*)\"/, async(expected) => {
            const pageTitle = await driver.findElement('.govuk-heading-l');
            const actual = await pageTitle.getText()
            expect(actual).toEqual(expected)
            driver.quit();
        });
    });
});