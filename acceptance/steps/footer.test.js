const JestCucumber = require('jest-cucumber')
const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

const screen = {
  width: 1024,
  height: 768
};

const feature = JestCucumber.loadFeature('features/footer.feature');

JestCucumber.defineFeature(feature, test => {
  test('Footer contains link to privacy policy', ({ given, when, then }) => {

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

    when('I visit the Cyber Health Framework site', async () => {
      url = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`
      await driver.get(url).catch(urlCaptureException => { console.error(urlCaptureException) })
    });

    then(/I see a link to \"(.*)\" in the footer/, async (expected) => {
      const footerElement = await driver.findElement(WebDriver.By.css(`footer a[href="${expected}"]`));
      const actualFooterElement = await footerElement.getText();
      expect(actualFooterElement).toEqual('Privacy');
      driver.quit();
    });
  });
});