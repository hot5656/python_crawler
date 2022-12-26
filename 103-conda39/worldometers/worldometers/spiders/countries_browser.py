import scrapy


class CountriesBrowserSpider(scrapy.Spider):
    name = 'countries_browser'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/']

    def parse(self, response):
        pass
