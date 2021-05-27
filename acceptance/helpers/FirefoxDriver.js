const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');


class FirefoxDriver {
    constructor() {
        this.driver = this.buildFirefoxDriver({
            width: 1024,
            height: 768
        })
        this.baseUrl = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`;

        this.username = `${process.env.TEST_USERNAME}`
        this.password = `${process.env.TEST_PASSWORD}`
    }

    buildFirefoxDriver(screen) {

        const driver = new WebDriver.Builder()
            .withCapabilities(WebDriver.Capabilities.firefox())
            .setFirefoxOptions(new firefox.Options()
                .headless()
                .windowSize(screen)
            )
            .build();

        return driver;
    }


    async visitPage(resource) {
        const url = `${this.baseUrl}/${resource}`

        await this.driver.get(url).catch(urlCaptureException => {
            console.error(urlCaptureException)
        })


        let page_url = await this.driver.getCurrentUrl();

        if (page_url.includes("account")) {

            console.log("logging in", page_url);
            await this.driver.findElement(WebDriver.By.id('id_username')).sendKeys(this.username);
            await this.driver.findElement(WebDriver.By.id('id_password')).sendKeys(this.password);
            await this.driver.findElement(WebDriver.By.id('button_login')).click();


            // await this.driver.wait(WebDriver.until.urlIs(url));
            let new_page_url = await this.driver.getCurrentUrl();

            console.log("Logged in to this page: ", new_page_url);
        }


    }

    async findElement(cssSelector) {
        return await this.driver.findElement(WebDriver.By.css(cssSelector));
    }

    quit() {
        return this.driver.quit();
    }
}

module.exports = FirefoxDriver;