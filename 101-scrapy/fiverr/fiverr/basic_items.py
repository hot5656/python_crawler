import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup as beauty
import cloudscraper


class BasicItemsSpider(scrapy.Spider):
    name = 'basic_items'
    allowed_domains = ['www.fiverr.com']

    # def start_requests(self):
    #     yield scrapy.Request(url='https://www.fiverr.com/categories/online-marketin', callback=self.parse, headers={
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    #     })
    browser = cloudscraper.create_scraper(delay=10, browser='chrome')
    print("basic_items ==============")
    print(browser)
    print("==============")

    # scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
    # url = "https://www.fiverr.com/categories/online-marketing"

    # info_raw = scraper.get(url)
    # print("==============")
    # resp = Selector(info_raw)
    # print(resp)
    # print("==============")
    # items = resp.xpath("//a[@class='item-name']")
    # print(items)
    # print("==============")
    # for item in items:
    #     print(item.xpath(".//text()").get())

    def parse(self, response):
        items = response.xpath("//a[@class='item-name']")
        for item in items:
            yield {
                'title' : item.xpath(".//text()").get()
            }
