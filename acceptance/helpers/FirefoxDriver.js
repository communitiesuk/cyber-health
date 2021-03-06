const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');
var fs = require('fs');


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
                .setPreference('accessibility.tabfocus', 7)
                .headless()
                .windowSize(screen)
            )
            .build();

        return driver;
    }


    async visitPage(resource, automaticLogin = true) {

        const url = `${this.baseUrl}/${resource}`

        await this.driver.get(url).catch(urlCaptureException => {
            console.error(urlCaptureException)
            console.trace()
        });
        if (automaticLogin) {
            await this.doLogin();
        }
    }

    async performLogin(username, password) {
        let page_url = await this.driver.getCurrentUrl();
        if (page_url.includes("account")) {
            await this.driver.findElement(WebDriver.By.id('id_username')).sendKeys(username);
            await this.driver.findElement(WebDriver.By.id('id_password')).sendKeys(password);
            await this.driver.findElement(WebDriver.By.id('button_login')).click();
        }
    }

    getUsername() {
        return this.username;
    }

    async doLogin() {
        await this.performLogin(this.getUsername(), this.password);
    }

    async findElement(cssSelector) {
        return await this.driver.findElement(WebDriver.By.css(cssSelector));
    }

    async findElementByXPath(xPathSelector) {
        return await this.driver.findElement(WebDriver.By.xpath(xPathSelector));
    }

    async findElementById(idSelector) {
        return await this.driver.findElement(WebDriver.By.id(idSelector));
    }


    async setIdtoValue(idSelector, value) {
        return await this.driver.findElement(WebDriver.By.id(idSelector)).sendKeys(value);
    }

    async getUrl() {
        return await this.driver.getCurrentUrl();
    }

    async getPageSource() {
        return await this.driver.getPageSource();
    }

    async getBaseUrl(resource) {
        return `${this.baseUrl}/${resource}`;
    }

    async clickLinkWithText(link_text) {
        await this.driver.findElement(WebDriver.By.xpath("//a[contains(.,'" + link_text + "')]")).click();

    }

    async clickButtonWithText(link_text) {
        await this.driver.findElement(WebDriver.By.xpath("//button[contains(.,'" + link_text + "')]")).click();
    }

    async pressKey(element, key) {
        await this.driver.findElement(WebDriver.By.css(element)).sendKeys(WebDriver.Key[key]);
    }

    async readTextFile(filePath) {
        return fs.readFileSync(filePath)
    }

    async GotoUrl(url) {
        return await this.driver.get(url)
    }

    quit() {
        return this.driver.quit();
    }
}

module.exports = FirefoxDriver;