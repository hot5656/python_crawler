import scrapy


class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'
    allowed_domains = ['slickdeals.net']
    start_urls = ['http://slickdeals.net/']

    def parse(self, response):
        pass
