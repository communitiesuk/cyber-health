const JestCucumber = require('jest-cucumber')
const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

const screen = {
  width: 1024,
  height: 768
};

const feature = JestCucumber.loadFeature('features/privacy-policy.feature');

JestCucumber.defineFeature(feature, test => {
  test('Privacy policy page contains expected heading', ({ given, when, then }) => {

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

    when('I visit the Cyber Health Framework site Privacy policy page', async () => {
      const urlStub = 'privacy-policy'
      url = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}/${urlStub}`
      await driver.get(url).catch(urlCaptureException => { console.error(urlCaptureException) })
    });

    then(/I see a page with the heading \"(.*)\"/, async (expected) => {
      const pageTitle = await driver.findElement(WebDriver.By.id('main-content'))
      const actual = await pageTitle.getText()
      expect(actual).toContain(expected)
      driver.quit();
    });
  });
});