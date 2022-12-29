import scrapy
from scrapy.exceptions import CloseSpider
import json


class EbookSpider(scrapy.Spider):
    name = 'ebooks'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12&offset=0']

    INCREMENT_BY = 12
    offset = 0

    def parse(self, response):
        resp = json.loads(response.body)

        ebooks = resp.get('works')
        print(ebooks)
        for ebook in ebooks:
            yield {
                'title': ebook.get('title'),
                'subject': ebook.get('subject')
            }

        if len(ebooks) == 0:
            raise CloseSpider("Reached last page...")


        self.offset  += self.INCREMENT_BY
        yield scrapy.Request(
            url=f'https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.offset}',
            callback = self.parse
        )
