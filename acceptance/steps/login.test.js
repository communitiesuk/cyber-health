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
            await driver.clickLinkWithText(link_text)
        });

        and('I provide a valid username and password and click login', async() => {
            await driver.doLogin();
        });

        then('I reach the index page', async() => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/assessment/");
            const pageTitle = await driver.findElement('h1');
            const actual = await pageTitle.getText()
            const expected = "Your Council Cyber Health Overview"
            expect(actual).toEqual(expected)
        });
    });


    test('Successfully login to access deep content', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit a page which requires a login', async() => {
            // visit home route
            await driver.visitPage('assessment/psn', false);
        });

        and('I provide a valid username and password and click login', async() => {
            await driver.doLogin();
        });

        then('I reach the desired page', async() => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/assessment/psn");
            const pageTitle = await driver.findElement('h1');
            const actual = await pageTitle.getText()
            const expected = "Public Sector Network"
            expect(actual).toEqual(expected)
        });
    });


    afterAll(() => {
        driver.quit();
    });
});