const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/gulp-build.feature');

JestCucumber.defineFeature(feature, test => {
  let driver;

  test('CSS file exists at build target', ({
    given,
    when,
    then
  }) => {

    given('I am able to view a web page', () => {
      driver = new FirefoxDriver();
    });

    when('I visit the base URL', async () => {
      await driver.visitPage('')
    });

    then(/^I see a header with the background color of "(.*)"$/, async (expectedColour) => {
      const headerElement = await driver.findElement('.govuk-header');
      const headerBackgroundColor = await headerElement.getCssValue('background-color');
      expect(headerBackgroundColor).toEqual(expectedColour);
    });
  });
});