const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/footer.feature');

JestCucumber.defineFeature(feature, test => {
  let driver;

  beforeAll(() => {
    driver = new FirefoxDriver();
  });

  test('Footer contains link to privacy policy', ({ given, when, then }) => {
    given('I am a Cyber Capable Person', () => {});

    when('I visit the Cyber Health Framework site', async () => {
      // visit home route
      await driver.visitPage('');
    });

    then(/I see a link to \"(.*)\" in the footer/, async (expected) => {
      const footerElement = await driver.findElement(`footer a[href="${expected}"]`);
      const actualFooterElement = await footerElement.getText();
      expect(actualFooterElement).toEqual('Privacy');
      // driver.quit();
    });
  });

  test('Footer contains link to cookie policy', ({ given, when, then }) => {
    given('I am a Cyber Capable Person', () => {});

    when('I visit the Cyber Health Framework site', async () => {
      // visit home route
      await driver.visitPage('');
    });

    then(/I see a link to \"(.*)\" in the footer/, async (expected) => {
      const footerElement = await driver.findElement(`footer a[href="${expected}"]`);
      const actualFooterElement = await footerElement.getText();
      expect(actualFooterElement).toEqual('Cookies');
      // driver.quit();
    });
  });

  test('Footer contains link to Accessibility statement', ({ given, when, then }) => {
    given('I am a Cyber Capable Person', () => {});

    when('I visit the Cyber Health Framework site', async () => {
      // visit home route
      await driver.visitPage('');
    });

    then(/I see a link to \"(.*)\" in the footer/, async (expected) => {
      const footerElement = await driver.findElement(`footer a[href="${expected}"]`);
      const actualFooterElement = await footerElement.getText();
      expect(actualFooterElement).toEqual('Accessibility statement');
      // driver.quit();
    });

  });

  afterAll(() => {
    driver.quit();
  });
});