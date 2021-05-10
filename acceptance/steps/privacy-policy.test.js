const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/privacy-policy.feature');

JestCucumber.defineFeature(feature, test => {
  test('Privacy policy page contains expected heading', ({ given, when, then }) => {
    let driver;

    given('I am a Cyber Capable Person', () => {
      driver = new FirefoxDriver();
    });

    when('I visit the Cyber Health Framework site Privacy policy page', async () => {
      await driver.visitPage('privacy-policy');
    });

    then(/I see a page with the heading \"(.*)\"/, async (expected) => {
      const pageTitle = await driver.findElement('#main-content');
      const actual = await pageTitle.getText()
      expect(actual).toContain(expected)
      driver.quit();
    });
  });
});