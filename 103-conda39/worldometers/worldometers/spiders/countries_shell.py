import scrapy


class CountriesShellSpider(scrapy.Spider):
    name = 'countries_shell'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/']

    def parse(self, response):
        pass
