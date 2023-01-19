import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['ithelp.ithome.com.tw']
    start_urls = ['https://ithelp.ithome.com.tw/articles?tab=tech']

    def parse(self, response):
        pass
