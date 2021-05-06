const AxeBuilder = require('@axe-core/webdriverjs');
const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

const baseUrl = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`
const pagesToAnalyze = [
    '/',
    'accessibility-statement',
    'cookie-policy',
    'privacy-policy',
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
            console.log(result);
        }).catch(err => {
            console.err(err);
        });
    });
}

async function analyzePage(driver, url) {
    try {
        await driver.get(url);
        const axe = new AxeBuilder(driver, null, { noSandbox: true });
        let result = await axe.analyze();
        return Promise.resolve(result);
    }
    catch (err) {
        return Promise.reject(err);
    }
}

runAccessibilityAnalysis(pagesToAnalyze);