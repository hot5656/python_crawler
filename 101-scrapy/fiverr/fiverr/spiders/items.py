import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ItemsSpider(CrawlSpider):
    name = 'items'
    allowed_domains = ['www.fiverr.com']
    # start_urls = ['https://www.fiverr.com/categories/online-marketing?source=category_tree']
    start_urls = ['https://www.fiverr.com/categories/online-marketing']
    # start_urls = ['https://104.18.254.23/categories/online-marketing']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='item-name']"), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths="//a[@class='currency-name-container link-secondary']"), callback='parse_item', follow=True),
    )

# class CoinsSpider(CrawlSpider):
#     name = 'coins'
#     allowed_domains = ['web.archive.org']
#     start_urls = ['https://web.archive.org/web/20190101085451/https://coinmarketcap.com/']

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//a[@class='currency-name-container link-secondary']"), callback='parse_item', follow=True),
#     )

    def parse_item(self, response):
        print("00 =============")
        # yield {
        #     "title" : response.xpath("//h1").get()
        # }
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
