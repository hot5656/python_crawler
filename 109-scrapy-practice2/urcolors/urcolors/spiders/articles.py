import scrapy
import json


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['urcolors.com.tw']
    # start_urls = ['https://urcolors.com.tw/posts']
    start_urls = ['https://urcolors.com.tw/_next/data/PUSKV8_Mq1g3g-Vz8kbh5/index.json']
    index = 0

    def parse(self, response):
        resp_dict = json.loads(response.body)
        posts = resp_dict.get('pageProps').get('posts').get('result')
        # print(posts)
        for post in posts:
            image_name = post.get('titleImage').get('asset').get('_ref').replace('image-', '').replace('-', '.')
            self.index +=1
            # yield {
            #     'index': self.index,
            #     'title': post.get('title'),
            #     'category': post.get('category'),
            #     'date': post.get('publishedAt'),
            #     'url': f"https://urcolors.com.tw/post/{post.get('slug')}",
            #     'image_url': image_name
            # }
            url = f"https://urcolors.com.tw/post/{post.get('slug')}"
            yield scrapy.Request(
                    url=url,
                    callback=self.parse_deep,
                    meta = {
                        'index': self.index,
                        'title': post.get('title'),
                        'category': post.get('category'),
                        'date': post.get('publishedAt'),
                        'url': url,
                    }
                )

    def parse_deep(self, response):
        momre_url = ''
        more_title = ''
        h3s = response.xpath('//h3')
        for h3 in h3s:
            h3_title = h3.xpath('.//text()').get()
            # print(h3_title)
            if h3_title == '延伸閱讀':
                # print(f"---{h3_title}")
                # print(h3.xpath(".//following:p/a/@href"))
                # print(h3.xpath(".//following-sibling::p/a/@href").get())
                # print(h3.xpath(".//following-sibling::p/a/strong/text()").get())
                more_title = h3.xpath(".//following-sibling::p/a/strong/text()").get()
                momre_url = h3.xpath(".//following-sibling::p/a/@href").get()
                break


        yield {
            'index': response.request.meta['index'],
            'title': response.request.meta['title'],
            'category': response.request.meta['category'],
            'date': response.request.meta['date'],
            'url': response.request.meta['url'],
            'image_url': response.xpath("//div[@class='post-thumbnailthumbnail']/img/@src").get(),
            'more_title': more_title,
            'momre_url': momre_url
        }
