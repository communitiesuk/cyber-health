const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/accessibility-statement.feature');

JestCucumber.defineFeature(feature, test => {
  test('Accessibility statement page contains expected heading', ({ given, when, then }) => {
    let driver;

    given('I am a Cyber Capable Person interested in accessibility', () => {
      driver = new FirefoxDriver();
    });

    when('I visit the Cyber Health Framework site Accessibility statement page', async () => {
      await driver.visitPage('accessibility-statement');
    });

    then(/I see a page with the heading \"(.*)\"/, async (expected) => {
      const pageTitle = await driver.findElement('#main-content');
      const actual = await pageTitle.getText()
      expect(actual).toContain(expected)
      driver.quit();
    });
  });
});
