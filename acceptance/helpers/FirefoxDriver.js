const WebDriver = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');


class FirefoxDriver {
  defaultScreen = {
    width: 1024,
    height: 768
  }
  defaultBaseUrl = `${process.env.FRONTEND_PROTO}://${process.env.FRONTEND_HOST}:${process.env.FRONTEND_PORT}`;

  constructor(screen = this.defaultScreen, baseUrl=this.defaultBaseUrl) {
    this.driver = this.buildFirefoxDriver(screen)
    this.screen = screen;
    this.baseUrl = baseUrl;
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
    return await this.driver.get(url).catch(urlCaptureException => {
      console.error(urlCaptureException)
    })
  }

  async findElement(cssSelector) {
    return await this.driver.findElement(WebDriver.By.css('#main-content'));
  }

  quit() {
    return this.driver.quit();
  }
}

module.exports = FirefoxDriver;