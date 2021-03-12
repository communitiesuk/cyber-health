const AxeBuilder = require('@axe-core/webdriverjs');
const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

const screen = {
    width: 1024,
    height: 768
};

driver = new WebDriver.Builder()
    .withCapabilities(WebDriver.Capabilities.firefox())
    .setFirefoxOptions(new firefox.Options()
        .headless()
        .windowSize(screen)
    )
    .build();

let url = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`

console.log(url);
console.log(process);

driver.get(url).then(() => {
    const axe = new AxeBuilder(driver, null, { noSandbox: true });
    axe.analyze(async(err, results) => {
        if (err) {
            // Handle error somehow
            console.error(results);
            process.exit(1);
        }
        console.log(results);
        await driver.quit();
    });
});