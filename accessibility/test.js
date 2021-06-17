const AxeBuilder = require('@axe-core/webdriverjs');
const WebDriver = require('selenium-webdriver'),
    By = WebDriver.By;
const firefox = require('selenium-webdriver/firefox');

const username = `${process.env.TEST_USERNAME}`
const password = `${process.env.TEST_PASSWORD}`
const baseUrl = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`
const pagesToAnalyze = [
    '/',
    'accessibility-statement',
    'account/account_activated/',
    'account/create-an-account',
    'account/login',
    'account/logout',
    'assessment',
    'assessment/psn',
    'cookie-policy',
    'privacy-policy',
    'account/password_reset',
    'account/password_reset_confirm_email'
]

const pagesRequireLogin = [
    'assessment',
    'assessment/psn',
]

const screen = {
    width: 1024,
    height: 768
};

const buildDriver = () => {
    return new WebDriver.Builder()
        .withCapabilities(WebDriver.Capabilities.firefox())
        .setFirefoxOptions(new firefox.Options()
            .headless()
            .windowSize(screen)
        )
        .build();
}

function runAccessibilityAnalysis(pages) {
    const urls = pages.map(page => new URL(page, baseUrl))
    urls.forEach(url => {
        let driver = buildDriver();
        analyzePage(driver, url).then(result => {
            if (result.violations.length === 0) {
                console.log("No Violations:", url.href);
            } else {
                console.warn("Violations:", url.href, result.violations);
            }
        }).catch(err => {
            console.error(err);
        });
    });
}

async function analyzePage(driver, url) {
    try {
        await driver.get(url);
        let page_url = await driver.getCurrentUrl();
        if (pagesRequireLogin.includes(page_url)) {
            await driver.findElement(By.id('id_username')).sendKeys(username);
            await driver.findElement(By.id('id_password')).sendKeys(password);
            await driver.findElement(By.id('button_login')).click();
        }
        const axe = new AxeBuilder(driver, null, { noSandbox: true });
        let result = await axe.analyze();
        return Promise.resolve(result);
    } catch (err) {
        return Promise.reject(err);
    }
}

runAccessibilityAnalysis(pagesToAnalyze);