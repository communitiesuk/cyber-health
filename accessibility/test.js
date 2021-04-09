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
console.log("****************************************************")
console.log(process.env.FRONTEND_PROTO)
console.log(process.env.FRONTEND_HOST)
console.log(process.env.FRONTEND_PORT)
console.log("****************************************************")

let url2 = process.env.FRONTEND_PROTO + "://" + process.env.FRONTEND_HOST + ":" + process.env.FRONTEND_PORT
let url = "http://localhost:8081"
console.log("This is the URL:" + url)
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