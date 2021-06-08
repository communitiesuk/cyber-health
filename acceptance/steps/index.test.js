const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/index.feature');

JestCucumber.defineFeature(feature, test => {
    let driver;

    beforeEach(() => {
        driver = new FirefoxDriver();
    });
    
    test('Index page contains expected heading', ({ given, when, then }) => {

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
        });
    });

    test('Index page contains skip to main content link', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {
            driver = new FirefoxDriver();
        });

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('');
        });

        and(/^I hit the "(.*)" key$/, async(key) => {
            await driver.pressKey('body', key.toUpperCase())
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        then('I jump to the main section', async() => {
            const { pathname, hash } = new URL(await driver.getUrl());
            const urlBarContent = `${pathname}${hash}`
            expect(urlBarContent).toEqual("/#main-content");
        });
    });

    afterEach(() => {
        driver.quit();
    });
});



