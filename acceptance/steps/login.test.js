const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/login.feature');

JestCucumber.defineFeature(feature, test => {
    let driver;

    beforeAll(() => {
        driver = new FirefoxDriver();
    });

    test('Successful from start', ({ given, when, then, and }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            // visit home route
            await driver.visitPage('');
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.findElementByXPath("//a[contains(.,'" + link_text + "')]").click();
        });

        and('I provide a valid username and password and click login', async() => {
            await driver.doLogin();
        });

        then('I reach the index page', async() => {
            const pageTitle = await driver.findElement('h1');
            const actual = await pageTitle.getText()
            expect(actual).toEqual(expected)
        });
    });


    afterAll(() => {
        driver.quit();
    });
});