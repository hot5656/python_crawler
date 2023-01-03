import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ItemsSpider(CrawlSpider):
    name = 'crawl_items'
    allowed_domains = ['www.fiverr.com']
    # start_urls = ['https://www.fiverr.com/categories/online-marketing?source=category_tree']
    start_urls = ['https://www.fiverr.com/categories/online-marketing']

    rules = (
        # Rule(LinkExtractor(restrict_xpaths="//a[@class='item-name']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print("00 =============")
        print(response.text())
        # yield {
        #     "title" : response.xpath("//h1").get()
        # }

