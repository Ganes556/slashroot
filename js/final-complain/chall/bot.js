import puppeteer from "puppeteer";

export const runBot =  async (username) => {
    const browser = await puppeteer.launch({
        headless: true,
        executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || null,
        args: ['--no-sandbox', '--headless', '--disable-gpu', '--disable-dev-shm-usage']
    })
    const page = await browser.newPage()
    await page.goto("http://localhost:20203/")
    await page.type("#username","admin")
    await page.type("#password","c6d8feccacae78e572c3eed8972e6fa61e164b97b510335ef0")
    await page.click(".btn")     

    const cookies = (await page.cookies());
    const page2 = await browser.newPage()

    await page2.setCookie(...cookies)    
    await page2.goto("http://localhost:20203/complain/" + username)
    
    // await browser.close();
}