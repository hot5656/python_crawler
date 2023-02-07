import scrapy
from scrapy_splash import SplashRequest
import ppt.items as items
from scrapy.loader import ItemLoader
import urllib
import os


class BeautySpider(scrapy.Spider):
    JPG = '.jpg'
    PNG = '.png'
    IMAGE_FOLDER = 'images'
    IMAGE_MAX = 5
    name = 'beauty'
    allowed_domains = ['www.ptt.cc']
    URL_ENTRY = 'https://www.ptt.cc/bbs/Beauty/index.html'
    index = 1

    # change to record cookie
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

            local element = splash:select('.over18-button-container > button')
            element:mouse_click()
            assert(splash:wait(1))

            return {
                cookies = splash:get_cookies(),
                html = splash:html(),
            }
        end
    '''

    # change to record cookie
    script_2nd = '''
        function main(splash, args)
            splash:init_cookies(splash.args.cookies)

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

            assert(splash:wait(1))

            return {
                cookies = splash:get_cookies(),
                html = splash:html(),
            }
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

        # change to record cookie
        self.cookies = response.data['cookies']
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

                    # change to record cookie
                    yield SplashRequest(url=response.urljoin(beaudy_item['url']),
                        callback=self.post_parse,
                        endpoint='execute',
                        args={'lua_source': self.script_2nd},
                        cookies = self.cookies
                        )

    def post_parse(self, response):
        # change to record cookie
        self.cookies = response.data['cookies']
        if self.index < self.IMAGE_MAX:
            title = response.xpath("(//div[@class='article-metaline']//span[@class='article-meta-value'])[2]/text()").get()
            lists = response.xpath("//div[@class='richcontent']")
            list_index = 1
            for list in lists:
                image_url = list.xpath(".//img/@src").get()
                loader = ItemLoader(item=items.PptPostItem())
                loader.add_value('image_urls', [image_url])
                loader.add_value('index', self.index)
                if self.PNG in image_url:
                    file_name = f"{title}{list_index}{self.PNG}"
                elif self.JPG in image_url:
                    file_name = f"{title}{list_index}{self.JPG}"
                else:
                    file_name = f"{title}{list_index}None{self.JPG}"
                list_index += 1

                self.image_download(image_url, file_name, self.IMAGE_FOLDER)
                self.index += 1
                yield loader.load_item()

                if self.index > self.IMAGE_MAX:
                    break

    def image_download(self, url, name, folder):
        dir=os.path.abspath(folder)
        work_path=os.path.join(dir,name)
        print(f"-->{name}")
        # urllib.request.urlretrieve(url, work_path)

