const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = JestCucumber.loadFeature('features/register.feature');

JestCucumber.defineFeature(feature, test => {
    let driver;

    beforeAll(() => {
        driver = new FirefoxDriver();
    });

    test('Sad path - Council already registered', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('', false);
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        and('I use an email address using a domain that is a subsequent user related to a council in the CyberHealth framework', async() => {
            await driver.setIdtoValue("id_email", "secondtest@example.com");
        });

        and('I fill in the other details with valid information', async() => {
            await driver.setIdtoValue("id_last_name", "test");
            await driver.setIdtoValue("id_first_name", "test");
            await driver.setIdtoValue("id_password1", "125345gdfgDFEWEgdfg4345dfsfsf");
            await driver.setIdtoValue("id_password2", "125345gdfgDFEWEgdfg4345dfsfsf");

        });

        and(/^I click on the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text)

        });

        then(/^I see a warning that I cannot register "(.*)"$/, async(message) => {

            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/register/");
            const pageTitle = await driver.findElement('.alert.alert-info');
            const actual = await pageTitle.getText();
            expect(actual).toEqual(message)
        });
    });


    test('Sad Path - Weak password', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('', false);
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        and('I use an email address using a domain that is a subsequent user related to a council in the CyberHealth framework', async() => {
            await driver.setIdtoValue("id_email", "test@example.org");
        });

        and('I provide a weak password', async() => {
            await driver.setIdtoValue("id_password1", "123");
            await driver.setIdtoValue("id_password2", "123");
        });

        and('I fill in the other details with valid information', async() => {
            await driver.setIdtoValue("id_last_name", "test");
            await driver.setIdtoValue("id_first_name", "test");
        });

        and(/^I click on the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text)
        });

        then(/^I see a warning that I cannot register "(.*)"$/, async(message) => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/register/");
            const pageTitle = await driver.findElement('.invalid-feedback');
            const actual = await pageTitle.getText();
            expect(actual).toEqual(message)
        });
    });

    test('Sad path - Email address previously registered', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('', false);
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        and('I provide an email address using a domain that was previously registered and password and click register', async() => {
            await driver.setIdtoValue("id_email", "test@example.com");
        });

        and('I fill in the other details with valid information', async() => {
            await driver.setIdtoValue("id_last_name", "test");
            await driver.setIdtoValue("id_first_name", "test");
            await driver.setIdtoValue("id_password1", "125345gdfgDFEWEgdfg4345dfsfsf");
            await driver.setIdtoValue("id_password2", "125345gdfgDFEWEgdfg4345dfsfsf");
        });

        and(/^I click on the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text)

        });

        then(/^I see a warning that I cannot register "(.*)"$/, async(message) => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/register/");
            const pageTitle = await driver.findElement('.alert.alert-info');
            const actual = await pageTitle.getText();
            expect(actual).toEqual(message)
        });
    });

    test('Sad path - Email address is not associated to a council', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('', false);
        });

        and(/^I click on the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text)
        });

        and('I use an email address not using a domain related to a council in the CyberHealth framework', async() => {
            await driver.setIdtoValue("id_email", "test@gmail.com");
        });

        and('I fill in the other details with valid information', async() => {
            await driver.setIdtoValue("id_last_name", "test");
            await driver.setIdtoValue("id_first_name", "test");
            await driver.setIdtoValue("id_password1", "125345gdfgDFEWEgdfg4345dfsfsf");
            await driver.setIdtoValue("id_password2", "125345gdfgDFEWEgdfg4345dfsfsf");
        });

        and(/^I click the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text)

        });

        then(/^I see a warning that I cannot be signed up "(.*)"$/, async(message) => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/register/");
            const pageTitle = await driver.findElement('.alert.alert-info');
            const actual = await pageTitle.getText();
            expect(actual).toEqual(message)
        });
    });

    afterAll(() => {
        driver.quit();
    });
});