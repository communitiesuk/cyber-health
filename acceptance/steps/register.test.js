const JestCucumber = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');
const path = require('path');

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
            await driver.setIdtoValue("id_name", "test");
            await driver.setIdtoValue("id_password1", "125345gdfgDFEWEgdfg4345dfsfsf");
            await driver.setIdtoValue("id_password2", "125345gdfgDFEWEgdfg4345dfsfsf");

        });

        and(/^I click on the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text)

        });

        then(/^I see a warning that I cannot register "(.*)"$/, async(message) => {

            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/create-an-account/");
            const errorMessage = await driver.findElement(".govuk-error-summary");
            const actual = await errorMessage.getText()
            expect(actual).toContain(message)
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
            await driver.setIdtoValue("id_name", "test");
        });

        and(/^I click on the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text)
        });

        then(/^I see a warning that I cannot register "(.*)"$/, async(message) => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/create-an-account/");
            // const pageTitle = await driver.findElement('.invalid-feedback');
            const errorMessage = await driver.findElement(".govuk-error-summary");
            const actual = await errorMessage.getText();
            expect(actual).toContain(message)
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
            await driver.setIdtoValue("id_name", "test");
            await driver.setIdtoValue("id_password1", "125345gdfgDFEWEgdfg4345dfsfsf");
            await driver.setIdtoValue("id_password2", "125345gdfgDFEWEgdfg4345dfsfsf");
        });

        and(/^I click on the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text)

        });

        then(/^I see a warning that I cannot register "(.*)"$/, async(message) => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/create-an-account/");
            const errorMessage = await driver.findElement(".govuk-error-summary");
            const actual = await errorMessage.getText();
            expect(actual).toContain(message)
        });
    });

    test('Sad path - Email address is not associated to a council', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('', false);
        });

        and(/^I click on the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text);
        });

        and('I use an email address not using a domain related to a council in the CyberHealth framework', async() => {
            await driver.setIdtoValue("id_email", "test@gmail.com");
        });

        and('I fill in the other details with valid information', async() => {
            await driver.setIdtoValue("id_name", "test");
            await driver.setIdtoValue("id_password1", "125345gdfgDFEWEgdfg4345dfsfsf");
            await driver.setIdtoValue("id_password2", "125345gdfgDFEWEgdfg4345dfsfsf");
        });

        and(/^I click the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text);

        });

        then(/^I see a warning that I cannot be signed up "(.*)"$/, async(message) => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/create-an-account/");
            const errorMessage = await driver.findElement(".govuk-error-summary");
            const actual = await errorMessage.getText()
            expect(actual).toContain(message)
        });
    });

    test('Sad Path - Commonly used password', ({ given, when, and, then }) => {

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('', false);
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text);
        });

        and('I use an email address using a domain that is a first user related to a council in the CyberHealth framework', async() => {
            await driver.setIdtoValue("id_email", "test@example.com");
        });

        and('I provide a commonly used password', async() => {
            await driver.setIdtoValue("id_password1", "password");
            await driver.setIdtoValue("id_password2", "password");
        });

        and('I fill in the other details with valid information', async() => {
            await driver.setIdtoValue("id_name", "test");
        });

        and(/^I click on the "(.*)" button$/, async(link_text) => {
            await driver.clickButtonWithText(link_text);
        });

        then(/^I see a warning that I cannot register "(.*)"$/, async(message) => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/account/create-an-account/");
            const errorMessage = await driver.findElement(".govuk-error-summary");
            const actual = await errorMessage.getText();
            expect(actual).toContain(message)
        });
    });

    test('Happy path - Success within one session', ({ given, when, and, then }) => {
        let url;
        const username = "test@gov.org.uk";
        const password = "125345gdfgDFEWEgdfg4345dfsfsf";

        given('I am a Cyber Capable Person', () => {});

        when('I visit the Cyber Health Framework site', async() => {
            await driver.visitPage('', false);
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text);
        });

        and('I use an email address using a domain that is a first user related to a council in the CyberHealth framework', async() => {
            await driver.setIdtoValue("id_email", username);
        });

        and('I fill in the other details with valid information', async() => {
            await driver.setIdtoValue("id_name", "test");
            await driver.setIdtoValue("id_password1", password);
            await driver.setIdtoValue("id_password2", password);
        });

        and(/^I click on the "(.*)" button$/, async(link_text) => {
            process.env['GOVUK_NOTIFY_DISABLE'] = true;
            await driver.clickButtonWithText(link_text);
        });

        and('I am asked to use my email to show that I am a user with access to the council email account', async() => {
            const filePath = path.join(__dirname, "../../CyberHealth/Spooler/url.txt");
            url = await driver.readTextFile(filePath);
        });

        and('On the same browser I use that confirmation link and account is activated', async() => {
            token = String(url).split('/').slice(-1).pop();
            console.log(token);
            url = await driver.getBaseUrl(`account/account_verification/${token}`);
            console.log(url);
            await driver.GotoUrl(url);
            console.log(await driver.getUrl());
            expect(new URL(await driver.getUrl()).pathname).toEqual(expect.stringContaining("/account/account_activated/"));
            const pageTitle = await driver.findElement('h1');
            const actual = await pageTitle.getText()
            const expected = "Your account is now ready for use"
            expect(actual).toEqual(expected)
        });

        and(/^I click the "(.*)" link$/, async(link_text) => {
            await driver.clickLinkWithText(link_text);
            await driver.performLogin(username, password);
        });

        then('I can login and see the assessment council overview screen', async() => {
            expect(new URL(await driver.getUrl()).pathname).toEqual("/assessment/");
            const pageTitle = await driver.findElement('h1');
            const actual = await pageTitle.getText()
            const expected = "Your Council Cyber Health Overview"
            expect(actual).toEqual(expected)
        });
    });

    afterAll(() => {
        driver.quit();
    });
});