import scrapy
from scrapy_splash import SplashRequest


class SearchPhoneSpider(scrapy.Spider):
    name = 'search_phone'
    allowed_domains = ['m.momoshop.com.tw']
    URL_ENTRY = 'https://m.momoshop.com.tw/main.momo'
    # URL_ENTRY = 'https://www.ptt.cc/bbs/Beauty/index.html'

    script = '''
        function main(splash, args)
            splash:on_request(function(request)
                if request.url:find('css') then
                    request.abort()
                end
            end)
            splash.images_enabled = false
            -- need run js for click     --
            -- splash.js_enabled = false --

            assert(splash:go(args.url))
            assert(splash:wait(10))

            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url=self.URL_ENTRY,
                            callback=self.parse,
                            endpoint='execute',
                            args={'lua_source': self.script})

    def parse(self, response):
        with open('index.html', 'wb') as f:
            f.write(response.body)
