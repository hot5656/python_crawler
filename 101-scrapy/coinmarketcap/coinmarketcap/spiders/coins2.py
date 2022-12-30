import scrapy
from scrapy_splash import SplashRequest, SplashFormRequest


class Coins2Spider(scrapy.Spider):
    name = 'coins2'
    allowed_domains = ['web.archive.org']
    # start_urls = ['https://web.archive.org/web/20190101085451/https://coinmarketcap.com/']

    script = '''
        -- https://web.archive.org/web/20190101085451/https://coinmarketcap.com/
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(5))
            return splash:html()
        end
    '''

    script2 = '''
        -- https://web.archive.org/web/20190101085451/https://coinmarketcap.com/
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(1))
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url='https://web.archive.org/web/20190101085451/https://coinmarketcap.com/',
            endpoint='execute',
            args = {
                'lua_source': self.script
            },
            callback=self.parse
        )

    def parse(self, response):
        coins = response.xpath("//a[@class='currency-name-container link-secondary']")
        for coin in coins:
            # print("============")
            # print(coin.xpath(".//@href").get())
            # print(coin)
            # yield {
            #     'url': coin.xpath(".//@href").get(),
            #     'name': coin.xpath(".//text()").get()
            # }
            print("2============")
            yield SplashRequest(
                url = f'https://web.archive.org{coin.xpath(".//@href").get()}',
                endpoint='execute',
                # args = {
                #     'timeout':8,
                #     'images':0
                # },
                args = {
                    'lua_source': self.script2
                },
                callback=self.parse_next
            )
            # yield SplashRequest(url=absolute_url, callback=self.parse, endpoint="execute", args={
            #     'lua_source': self.script
            # })
            # print("3============")
            # print(coin.xpath(".//tetx()"))

    def parse_next(self, response):
        # print("4============")
        # print(response.xpath("normalize-space((//h1/text())[2])").get())
        yield {
            'name': response.xpath("normalize-space((//h1/text())[2])").get(),
            'rank': response.xpath("//span[@class='label label-success']/text()").get(),
            'price(USD)': response.xpath("//span[@class='h2 text-semi-bold details-panel-item--price__value']/text()").get()
        }

