const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/pathway.feature');

JestCucumber.defineFeature(feature, test => {
    let driver;

    beforeAll(() => {
        driver = new FirefoxDriver();
    });

    test('Pathway page contains expected text', ({ given, when, then }) => {
        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework pathway page', async() => {
            await driver.visitPage('assessment/psn')
        });

        then(/I see the text \"(.*)\"/, async(expected) => {
            const pageTitle = await driver.findElement('h1');
            const actual = await pageTitle.getText()
            expect(actual).toEqual(expected)
        });
    });
    
    afterAll(() => {
        driver.quit();
    });

});
