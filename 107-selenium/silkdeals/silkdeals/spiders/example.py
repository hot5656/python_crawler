import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        # img = response.request.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']
        search_input = driver.find_element(By.XPATH, "//input[@id='search_form_input_homepage']")
        search_input.send_keys('Hello World')
        # screenshot after send "Hello World"
        # driver.save_screenshot('after_filling_input.png')

        search_input.send_keys(Keys.ENTER)
        # screenshot after press Enter
        # driver.save_screenshot('enter.png')

        html = driver.page_source
        response_obj = Selector(text=html)

        links = response_obj.xpath("//h2[@class='LnpumSThxEWMIsDdAT17 CXMyPcQ6nDv47DKFeywM']")
        for link in links:
            yield {
                'URL' : link.xpath(".//a/@href").get(),
                'Title' : link.xpath(".//span/text()").get()
            }
