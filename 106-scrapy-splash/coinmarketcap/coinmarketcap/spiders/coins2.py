import scrapy
from scrapy_splash import SplashRequest


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
        i = 1
        for coin in coins:
            print(f"({i})============")
            i += 1
            yield SplashRequest(
                url = f'https://web.archive.org{coin.xpath(".//@href").get()}',
                endpoint='execute',
                args = {
                    'lua_source': self.script2
                },
                callback=self.parse_next
            )

    def parse_next(self, response):
        print("next ============")
        yield {
            'name': response.xpath("normalize-space((//h1/text())[2])").get(),
            'rank': response.xpath("//span[@class='label label-success']/text()").get(),
            'price(USD)': response.xpath("//span[@class='h2 text-semi-bold details-panel-item--price__value']/text()").get()
        }
