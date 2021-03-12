import AxeBuilder from '@axe-core/webdriverjs';
import { Builder, Capabilities } from 'selenium-webdriver';
import { setDefaultService, ServiceBuilder, Options } from 'selenium-webdriver/chrome';
import { path } from 'chromedriver';


const screen = {
    width: 640,
    height: 480
};

setDefaultService(new ServiceBuilder(path).build());

var driver = new Builder()
    .withCapabilities(Capabilities.chrome())
    .setChromeOptions(new Options().headless().windowSize(screen))
    .build();


let url = `{process.env.FRONTEND_PROTO}://{process.env.FRONTEND_HOST}:process.env.FRONTEND_PORT/`

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