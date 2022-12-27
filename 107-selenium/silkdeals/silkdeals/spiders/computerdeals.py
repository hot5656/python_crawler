import scrapy
from scrapy_selenium import SeleniumRequest

class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'

    # remove 0xa0 - it's noot nned just for try
    def remove_characters(self, value):
        return value.strip('\xa0')

    def start_requests(self):
        yield SeleniumRequest(
            url='https://slickdeals.net/computer-deals/',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals blueprint']/li")
        for product in products:
            base_url = "https://slickdeals.net/computer-deals"
            yield {
                'name': product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/text()").get(),
                'link': base_url + product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/@href").get(),
                # 1st row store name's position
                # 'store_name': product.xpath(".//span[@class='blueprint']/a/text()").get(),
                # no add normalize-space, call remove_characters() not work
                # 'store_name': self.remove_characters(product.xpath(".//span[@class='blueprint']/button['itemStore bp-p-storeLink bp-c-linkableButton  bp-c-button js-button bp-c-button--link']/text()").get()),
                'store_name': self.remove_characters(product.xpath("normalize-space(.//span[@class='blueprint']/button['itemStore bp-p-storeLink bp-c-linkableButton  bp-c-button js-button bp-c-button--link']/text())").get()),
                'price': product.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get()
            }

        next_page = product.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            yield SeleniumRequest(
                url=f'https://slickdeals.net{next_page}',
                wait_time=3,
                callback=self.parse
            )

