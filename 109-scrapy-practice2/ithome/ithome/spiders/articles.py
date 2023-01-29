import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
from datetime import datetime


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['ithelp.ithome.com.tw']
    index = 0
    page_index = 1
    MAX_PAGE = 2
    URL_1ST = 'https://ithelp.ithome.com.tw/articles?tab=tech'

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(2))

            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url=self.URL_1ST, callback=self.parse, endpoint="execute",
        args={
            'lua_source': self.script
        })


    def parse(self, response):
        articles = response.xpath("//div[@class='board tabs-content']/div[@class='qa-list']")
        for article in articles:
            # yield {
            #     'url': article.xpath(".//a[@class='qa-list__title-link']/@href").get(),
            #     'title': article.xpath(".//a[@class='qa-list__title-link']/text()").get(),
            #     'author': article.xpath("normalize-space(.//a[@class='qa-list__info-link']/text())").get(),
            #     'publish_time': article.xpath(".//a[@class='qa-list__info-time']/@title").get(),
            #     # 'tags': article.xpath(".//a[@class='qa-list__title-link']/@href").get(),
            #     'content': article.xpath("normalize-space(.//p[@class='qa-list__desc']/text())").get(),
            #     'view_count': article.xpath("(.//span[@class='qa-condition__count'])[3]/text()").get(),
            # }
            article_date_str = article.xpath(".//a[@class='qa-list__info-time']/@title").get()
            article_date = datetime.strptime(article_date_str, '%Y-%m-%d %H:%M:%S')

            url = article.xpath(".//a[@class='qa-list__title-link']/@href").get()
            yield SplashRequest(url=url, callback=self.article_parse, endpoint="execute",
                meta = {
                    'url': article.xpath(".//a[@class='qa-list__title-link']/@href").get(),
                    'author': article.xpath("normalize-space(.//a[@class='qa-list__info-link']/text())").get(),
                    'publish_time': article_date,
                    'view_count': int(article.xpath("(.//span[@class='qa-condition__count'])[3]/text()").get()),
                },
                args={
                    'lua_source': self.script
            })

        self.page_index += 1
        if self.page_index <= self.MAX_PAGE:
            url = f'{self.URL_1ST}&page={self.page_index}'
            yield SplashRequest(url=url, callback=self.parse, endpoint="execute",
            args={
                'lua_source': self.script
            })

    def article_parse(self, response):
        tags_list= response.xpath("//a[@class='tag qa-header__tagList']/text()").getall()
        tags= ','.join(tags_list)
        content_html = response.xpath("//div[@class='markdown__style']").get()
        soup= ''
        content=''

        self.index +=1
        try:
            soup = BeautifulSoup(content_html, "html.parser")
            content = soup.get_text()
        except:
            print(f"{self.index}---------------->")

        content = self.content_alignment(content)
        article_responses = []
        # item_responses = response.xpath("//div[@class='ans-header']")
        # for item_response in item_responses:
        #     resp_date_str = item_response.xpath(".//a[@class='ans-header__time']/text()").get()
        #     resp_date = datetime.strptime(resp_date_str, '%Y-%m-%d %H:%M:%S')
        #     resp_content = item_response.xpath(".//parent::node()/div[@class='response-markdown']/div/div/p/text()").get()
        #     resp_content = self.content_alignment(resp_content)
        #     article_responses.append({
        #         'author': item_response.xpath(".//a[@class='response-header__person']/text()").get(),
        #         'content': resp_content,
        #         'publish_time': resp_date
        #     })

        item_responses = response.xpath("//div[@class='qa-panel response clearfix']")
        for item_response in item_responses:
            resp_date_str = item_response.xpath(".//a[@class='ans-header__time']/text()").get()
            resp_date = datetime.strptime(resp_date_str, '%Y-%m-%d %H:%M:%S')
            resp_content = item_response.xpath(".//div[@class='response-markdown']/div/div/p/text()").get()
            resp_id = int(item_response.xpath(".//a/@name").get().replace("response-", ""))
            article_responses.append({
                'resp_id': resp_id,
                'author': item_response.xpath(".//a[@class='response-header__person']/text()").get(),
                'content': resp_content,
                'publish_time': resp_date
            })
        yield {
            'index': self.index,
            'url': response.request.meta['url'],
            'author': response.request.meta['author'],
            'publish_time': response.request.meta['publish_time'],
            'view_count': response.request.meta['view_count'],
            'title': response.xpath("normalize-space(//h2[@class='qa-header__title']/text())").get(),
            'tags': tags,
            'content': content,
            'responses': article_responses
        }

    def content_alignment(self, content):
        # break into lines and remove leading and trailing space on each
        # lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        # content = '\n'.join(chunk for chunk in chunks if chunk)

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in content.splitlines())
        # drop blank lines
        content = '\n'.join(line for line in lines if line)

        return content
