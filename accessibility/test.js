const AxeBuilder = require('@axe-core/webdriverjs');
const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');
const {Builder, By} = require('selenium-webdriver');

const baseUrl = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`
const pagesToAnalyze = [
    '/',
    'accessibility-statement',
    'cookie-policy',
    'privacy-policy',
    'assessment',
    'assessment/psn'
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

const username = "CyberHealth"
const password = "cyber123"

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
        if (url.href.includes("assessment")) {
            await driver.findElement(By.id('id_username')).sendKeys(username);
            await driver.findElement(By.id('id_password')).sendKeys(password);
            await driver.findElement(By.css('button')).click();
        }
        const axe = new AxeBuilder(driver, null, { noSandbox: true });
        let result = await axe.analyze();
        return Promise.resolve(result);
    } catch (err) {
        return Promise.reject(err);
    }
}

runAccessibilityAnalysis(pagesToAnalyze);