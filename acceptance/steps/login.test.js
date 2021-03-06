const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/login.feature');

JestCucumber.defineFeature(feature, test => {
    let driver;

    beforeEach(() => {
        driver = new FirefoxDriver();
    });

    test('Successful from start', ({ given, when, then, and }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            // visit home route
            await driver.visitPage('', false);
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

    test('Successful from start and logout', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            // visit home route
            await driver.visitPage('', false);
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

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        then('I reach the logged out page', async() => {
            expect(new URL(await driver.getUrl()).pathname).toEqual(expect.stringContaining("/account/logout"));
        });

        and(/^I see a message "(.*)"$/, async(message) => {
            const pageTitle = await driver.findElement('h1');
            const actual = await pageTitle.getText()
            expect(actual).toEqual(message)
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        then('I reach the login page', async() => {
            expect(new URL(await driver.getUrl()).pathname).toEqual(expect.stringContaining("/account/login"));
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

    test('wrong password or username combination', ({ given, when, and, then }) => {
        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            // visit home route
            await driver.visitPage('');
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        and('I provide a combination of valid username and an invalid password and click login', async() => {
            await driver.performLogin(driver.getUsername(), "NOT THE RIGHT PASSWORD");
        });

        then('I see the login page', async() => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/login");

        });

        and('I see a message explaining that the credentials provided were incorrect', async() => {
            const pageTitle = await driver.findElement('ul.govuk-error-summary__list > li > a');
            const actual = await pageTitle.getText()
            const expected = "Enter a valid email and password combination. You will be locked out if you enter the wrong details 5 times."
            expect(actual).toEqual(expected)
        });
    });

    test('unknown username with password combination', ({ given, when, and, then }) => {
        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            // visit home route
            await driver.visitPage('');
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        and('I provide a combination of an unknown username and any password', async() => {
            await driver.performLogin("notauser@example.org", "Password123");
        });

        then('I see the login page', async() => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/login");

        });

        and('I see a message explaining that the credentials provided were incorrect', async() => {
            const pageTitle = await driver.findElement('ul.govuk-error-summary__list > li > a');
            const actual = await pageTitle.getText()
            const expected = "Enter a valid email and password combination. You will be locked out if you enter the wrong details 5 times."
            expect(actual).toEqual(expected)
        });
    });

    afterEach(() => {
        driver.quit();
    });
});