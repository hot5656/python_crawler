import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup as beauty
import cloudscraper


class BasicItemsSpider(scrapy.Spider):
    name = 'basic_items'
    allowed_domains = ['www.fiverr.com']
    # start_urls = ['https://www.fiverr.com/categories/online-marketin']

    # def start_requests(self):
    #     yield scrapy.Request(url='https://www.fiverr.com/categories/online-marketin', callback=self.parse, headers={
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    #     })

    scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
    url = "https://www.fiverr.com/categories/online-marketing"

    info_raw = scraper.get(url)
    # print("==============")
    # print(info_raw)
    # print("==============")
    # info = scraper.get(url).text
    # soup = beauty(info, "html.parser")
    # soup = beauty(info, "html5lib")
    print("10 ==============")
    resp = Selector(info_raw)
    print(resp)
    print("11 ==============")
    items = resp.xpath("//a[@class='item-name']")
    print(items)
    print("12 ==============")
    for item in items:
        print(item.xpath(".//text()").get())



        # yield {

        # }
        # yield {
        #     'title' : item.xpath(".//text()").get()
        # }
    # self.parse(Selector(soup))

    def parse(self, response):
        items = response.xpath("//a[@class='item-name']")
        for item in items:
            yield {
                'title' : item.xpath(".//text()").get()
            }
