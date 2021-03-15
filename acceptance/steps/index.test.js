const JestCucumber = require('jest-cucumber')
const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

const screen = {
    width: 1024,
    height: 768
};

const feature = JestCucumber.loadFeature('features/index.feature');

JestCucumber.defineFeature(feature, test => {
    test('Index page contains expected text', ({ given, when, then }) => {

        let url = "";
        let driver;

        given('I am a Cyber Capable Person', () => {
            driver = new WebDriver.Builder()
                .withCapabilities(WebDriver.Capabilities.firefox())
                .setFirefoxOptions(new firefox.Options()
                    .headless()
                    .windowSize(screen)
                )
                .build();
        });

        when('I visit the Cyber Health Framework site', async() => {
            url = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`
            console.log("Calling url: " + url)
            await driver.get(url).catch(urlCaptureException => { console.error(urlCaptureException) })
        });

        then(/I see the text \"(.*)\"/, async(expected) => {
            // do nothing
            const pageTitle = await driver.findElement(WebDriver.By.id('local-authority-cyber-health-framework'))
            const actual = await pageTitle.getText()
            expect(actual).toEqual(expected)
            driver.quit();
        });
    });
});