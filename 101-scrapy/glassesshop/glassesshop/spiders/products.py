import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']
    page_index = 1

    def parse(self, response):
        for product in response.xpath('//div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'):
            yield {
                'product_name': product.xpath('.//div[@class="p-title"]/a/text()').get().strip(),
                'product_price': product.xpath('.//div[@class="p-price"]/div/span/text()').get(),
                'product_url': product.xpath('.//div[@class="product-img-outer"]/a/@href').getall(),
                'product_image': product.xpath('.//img[@class="lazy d-block w-100 product-img-default"]/@data-src').get().split('?')[0],
                'page_number': self.page_index
            }

        self.page_index += 1
        next_page = response.xpath('//a[@class="page-link"][@rel="next"]/@href').get()
        if next_page:
            yield {
                'link' : next_page
            }
            yield scrapy.Request(url=next_page, callback=self.parse)



