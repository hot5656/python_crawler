# momo scrapy_selenium ok
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector

class MomoSpider(scrapy.Spider):
    name = "momo"
    # allowed_domains = ["www.momoshop.com.tw"]
    # start_urls = ["http://www.momoshop.com.tw/"]
    # https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone 14 pro&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType

            # url='https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone 14 pro&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType',
    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.momoshop.com.tw/search/searchShop.jsp',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        # with open('index.html', 'wb') as f:
        #     f.write(response.body)

        driver = response.meta['driver']
        search_input = driver.find_element(By.XPATH, "//input[@class='inputArea ac_input ui-autocomplete-input']")
        search_input.send_keys('iphone 14 pro')

        # screenshot after send "Hello World"
        # driver.save_screenshot('after_filling_input.png')

        search_input.send_keys(Keys.ENTER)
        # screenshot after press Enter
        # driver.save_screenshot('enter.png')

        # print("==================")
        # print(response.body)
        # print("==================")

        html = driver.page_source
        response_obj = Selector(text=html)
        products = response_obj.xpath("//div[@class='listArea']/ul/li")
        for product in products:
            yield {
                'product_name': product.xpath(".//h3/text()").get(),
                'price': product.xpath(".//span[@class='price']/b/text()").get(),
            }