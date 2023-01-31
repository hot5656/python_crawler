import scrapy
from scrapy_splash import SplashRequest
import ppt.items as items
from scrapy.loader import ItemLoader
import urllib


class BeautySpider(scrapy.Spider):
    name = 'beauty'
    allowed_domains = ['www.ptt.cc']
    URL_ENTRY = 'https://www.ptt.cc/bbs/Beauty/index.html'
    index = 1

    # local element = splash:select('.over18-button-container > button')
    script_1st = '''
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
            assert(splash:wait(0.5))

            local element = splash:select('body > div.bbs-screen.bbs-content.center.clear > form > div:nth-child(2) > button')
            element:mouse_click()
            assert(splash:wait(5))

            return splash:html()
        end
    '''

    script_2nd = '''
        function main(splash, args)
            splash:on_request(function(request)
                if request.url:find('css') then
                    request.abort()
                end
            end)
            splash.images_enabled = false
            splash.js_enabled = false

            assert(splash:go(args.url))
            assert(splash:wait(0.5))

            local element = splash:select('body > div.bbs-screen.bbs-content.center.clear > form > div:nth-child(2) > button')
            element:mouse_click()
            assert(splash:wait(5))

            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url=self.URL_ENTRY,
                            callback=self.parse,
                            endpoint='execute',
                            args={'lua_source': self.script_1st})

    def parse(self, response):
        # with open('index.html', 'wb') as f:
        #     f.write(response.body)
        posts = response.xpath("//div[@class='r-ent']")
        for post in posts:
            beaudy_item = items.PptBeautyItem()
            beaudy_item['title'] = post.xpath(".//div[@class='title']/a/text()").get()
            beaudy_item['url'] = post.xpath(".//div[@class='title']/a/@href").get()
            beaudy_item['push_count'] = post.xpath(".//div[@class='nrec']/span/text()").get()
            beaudy_item['author'] = post.xpath(".//div[@class='author']/text()").get()

            if beaudy_item['title']:
                # if '公告' in beaudy_item['title']:
                if '公告' not in beaudy_item['title']:
                    # yield beaudy_item

                    # also verify person over 18
                    yield SplashRequest(url=response.urljoin(beaudy_item['url']),
                        callback=self.post_parse,
                        endpoint='execute',
                        args={'lua_source': self.script_1st})

    def post_parse(self, response):
        # if self.index < 5:
        #     lists = response.xpath("//div[@class='richcontent']")
        #     for list in lists:
        #         # print(list.xpath(".//img/@src").get())
        #         image_url = list.xpath(".//img/@src").get()
        #         loader = ItemLoader(item=items.PptPostItem())
        #         loader.add_value('image_urls', image_url)
        #         loader.add_value('index', self.index)
        #         self.index += 1
        #         yield loader.load_item()
        if self.index < 5:
            lists = response.xpath("//div[@class='richcontent']")
            for list in lists:
                # item = items.PptPostItem()
                # image_url = list.xpath(".//img/@src").get()
                # item['image_urls'] = [image_url]
                # item['name'] = image_url
                # item['index'] = self.index
                # # print(f"({self.index} {image_url})")
                # self.index += 1
                # yield item

                # print(f"-->response.url")
                image_url = list.xpath(".//img/@src").get()
                loader = ItemLoader(item=items.PptPostItem())
                loader.add_value('image_urls', [image_url])
                loader.add_value('index', self.index)
                self.index += 1
                self.image_download(image_url, f"pic{self.index}", "images")
                yield loader.load_item()

                if self.index > 5:
                    break

    def image_download(self, url, name, folder):
        print(f"---> folder={folder} name={name} url={url}")
        urllib.request.urlretrieve(url, f"./{folder}/{name}")

