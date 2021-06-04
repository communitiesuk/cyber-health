const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/index.feature');

JestCucumber.defineFeature(feature, test => {
    test('Index page contains expected heading', ({ given, when, then }) => {
        let driver;

        given('I am a Cyber Capable Person', () => {
            driver = new FirefoxDriver();
        });

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('');
        });

        then(/I see a page with the heading \"(.*)\"/, async(expected) => {
            const pageTitle = await driver.findElement('#main-content');
            const actual = await pageTitle.getText()
            expect(actual).toContain(expected)
            driver.quit();
        });
    });

    test('Index page contains skip to main content link', ({ given, when, and, then }) => {
        let driver;

        given('I am a Cyber Capable Person', () => {
            driver = new FirefoxDriver();
        });

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('');
        });

        and('I hit the tab key', async(link_text) => {
            await driver.sendKeys(driver.keys.tab)
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        then(/I see a page with the heading \"(.*)\"/, async(expected) => {
            const pageTitle = await driver.findElement('#main-content');
            const actual = await pageTitle.getText()
            expect(actual).toContain(expected)
            driver.quit();
        });
    });
});



