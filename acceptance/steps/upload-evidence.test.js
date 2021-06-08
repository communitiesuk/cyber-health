const fs = require('fs');
const path = require('path');
const { loadFeature, defineFeature } = require('jest-cucumber')
const FirefoxDriver = require('../helpers/FirefoxDriver.js');

const feature = loadFeature('features/upload-evidence.feature');

defineFeature(feature, test => {
    let driver;

    beforeEach(() => {
        driver = new FirefoxDriver();
    });

    test('User uploads a document', ({
        given,
        and,
        when,
        then
    }) => {
        let rowsAtStart;
        let filename;
        let fileInput;
        
        given(/^I can access the "(.*)" page$/, async (pathname) => {
            await driver.visitPage(pathname)
        });

        and('I have a file available to upload', () => {
            filename = 'test-file.txt';
            fs.appendFile(filename, "file content goes here", (err) => {
                if (err) throw err;
                
                // file should have been created
                // test that it exists:
                fs.access(filename, fs.F_OK, (err) => {
                    if (err) throw err;
                    // file exists!
                    return;
                })
            });
        });

        and("I know how many files I have uploaded currently", async () => {
            const tableRows = await driver.findElementsByXPath("//table/tbody/tr");
            rowsAtStart = tableRows.length;
        })

        when(/^I click the "Choose file" button$/, async () => {
            fileInput = await driver.findElement("input[type=file]");
        });

        and('I select the file I want to upload', async () => {
            const filePath = path.resolve(filename);
            await fileInput.sendKeys(filePath);
        });

        and(/^I click the "(.*)" button$/, async (buttonText) => {
            await driver.clickButtonWithText(buttonText);
        });

        then('I can see my file in the list of uploaded files', async () => {
            const tableRows = await driver.findElementsByXPath("//table/tbody/tr");
            const numRows = tableRows.length;
            expect(numRows).toBe(rowsAtStart + 1);
            
        });
    });

    afterEach(() => {
        driver.quit();
    });
});