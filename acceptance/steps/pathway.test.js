const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/pathway.feature');

JestCucumber.defineFeature(feature, test => {
    test('Pathway page contains expected text', ({ given, when, then }) => {
        let driver;

        given('I am a Cyber Capable Person', () => {
            driver = new FirefoxDriver();
        });

        when('I visit the Cyber Health Framework pathway page', async() => {
            await driver.visitPage('assessment/psn')
        });

        then(/I see the text \"(.*)\"/, async(expected) => {
            const pageTitle = await driver.findElement('h1');
            const actual = await pageTitle.getText()
            expect(actual).toEqual(expected)
            driver.quit();
        });
    });
});