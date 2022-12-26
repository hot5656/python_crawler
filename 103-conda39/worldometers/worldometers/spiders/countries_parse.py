import scrapy


class CountriesParseSpider(scrapy.Spider):
    name = 'countries_parse'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/']

    def parse(self, response):
        pass
