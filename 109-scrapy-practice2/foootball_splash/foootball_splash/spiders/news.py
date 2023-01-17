import scrapy
from scrapy_splash import SplashRequest

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['foootball.cc']
    index = 0
    MAX_NEWS = 75

    script = '''
        function main(splash, args)
            -- no load css --
            splash:on_request(function(request)
                if request.url:find('css') then
                    request.abort()
                end
            end)
            -- no load image and js --
            splash.images_enabled = false
            splash.js_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return splash:html()
        end
    '''

    def start_requests(self):
        url = 'https://foootball.cc/'
        yield SplashRequest(url=url, callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })


    def parse(self, response):
        news = response.xpath("(//h2[@class='h2-title topic-line-four'])[2]/following::div/div[@class='row']")
        for new in news:
            if new.xpath(".//h4//a/text()").get()== None or (self.index >= self.MAX_NEWS):
                break

            self.index +=1
            image_url_str = new.xpath(".//div[@class='containerimg']/a/@style").get();
            image_url = image_url_str.split('(')[-1].split(')')[0];
            # yield {
            #     'title' : new.xpath(".//h4//a/text()").get(),
            #     'artical_url': new.xpath(".//h4/a/@href").get(),
            #     'image_url': image_url,
            #     'date': new.xpath("normalize-space(.//div[@class='mainnews-info-small']/span/text())").get(),
            #     'index': self.index
            # }

            yield SplashRequest(
                url=new.xpath(".//h4/a/@href").get(),
                callback=self.parse_article,
                endpoint="execute",
                args={
                    'lua_source': self.script
                },
                meta={
                    'index':self.index,
                    'title' : new.xpath(".//h4//a/text()").get(),
                    'artical_url': new.xpath(".//h4/a/@href").get(),
                    'image_url': image_url,
                    'date': new.xpath("normalize-space(.//div[@class='mainnews-info-small']/span/text())").get(),
            })

        next_page =  response.xpath("//a[@rel='next']/@href").get()
        if next_page and self.index < self.MAX_NEWS:
            print("=========================")
            print("--"+next_page+"--")
            yield SplashRequest(url=next_page, callback=self.parse, endpoint="execute", args={
                'lua_source': self.script
            })

    def parse_article(self, response):
        tags = response.xpath("//div[contains(@class, 'text-center')]/div/ul/li/h5/a/text()").getall()
        new_tags = [item.strip() for item in tags]
        
        yield {
            'index': response.request.meta['index'],
            'tags': new_tags,
            'title' : response.request.meta['title'],
            'artical_url': response.request.meta['artical_url'],
            'image_url': response.request.meta['image_url'],
            'date': response.request.meta['date'],
        }
