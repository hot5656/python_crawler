import scrapy
# from ..items import as items
import ithome2.items as items
from datetime import datetime


class ArticlesSpider(scrapy.Spider):
    URL_1ST = 'https://ithelp.ithome.com.tw/articles?tab=tech'
    MAX_PAGE = 2
    page_index = 1
    name = 'articles'
    allowed_domains = ['ithelp.ithome.com.tw']
    start_urls = [URL_1ST]

    def parse(self, response):
        # with open('ithome.html', 'wb') as f:
        #     f.write(response.body)

        articles = response.xpath("//div[@class='board tabs-content']/div[@class='qa-list']")
        for article in articles:
            article_url = article.xpath(".//a[@class='qa-list__title-link']/@href").get()
            yield response.follow(article_url, callback=self.article_parse)

        self.page_index += 1
        next_page = response.xpath("//a[@rel='next']/@href").get()
        if next_page and self.page_index <= self.MAX_PAGE :
            yield scrapy.Request(url=f"{self.URL_1ST}&page={self.page_index}", callback=self.parse)

    def article_parse(self, response):
        article_head = response.xpath("//div[@class='qa-header']")
        content = ''.join(response.xpath("//div[@class='markdown__style']/descendant::text()").getall())
        content = self.content_alignment(content)
        tags = article_head.xpath(".//a[contains(@class,'tag qa-header__tagList')]/text()").getall()
        author_list = article_head.xpath(".//a[@class='qa-header__info-person']/text()").getall()
        author = ''.join(x.strip() for x in author_list )

        article = items.IthomeArticleItem()
        article['url'] =  response.url
        article['author'] = author
        article['publish_time'] = article_head.xpath(".//a[@class='qa-header__info-time']/@title").get()
        article['view_count'] = int(article_head.xpath(".//span[@class='qa-header__info-view']/text()").get().split(" ")[0])
        article['title'] = article_head.xpath("normalize-space(.//h2[@class='qa-header__title']/text())").get()
        article['tags'] = ','.join(tags)
        article['content'] = content
        yield article

        if '_id' in article:
            '''
            上一行執行後資料已更新到資料庫中
            因為是同一個物件參照
            可以取得識別值
            '''
            article_id = article['_id']
            '''
            因為 iTHome 原文與回文都是在同一個畫面中
            剖析回文時使用原本的 response 即可
            否則這邊需要再回傳 Request 物件
            yield scrapy.Request(url, callback=self.parse_reply)
            '''
            yield from self.parse_reply(response, article_id)

    def parse_reply(self, response, article_id):
        item_responses = response.xpath("//div[@class='qa-panel response clearfix']")
        for item_response in item_responses:
            resp_date_str = item_response.xpath(".//a[@class='ans-header__time']/text()").get()
            resp_date = datetime.strptime(resp_date_str, '%Y-%m-%d %H:%M:%S')
            resp_content = item_response.xpath(".//div[@class='response-markdown']/div/div/p/text()").get()
            resp_id = int(item_response.xpath(".//a/@name").get().replace("response-", ""))

            article_resp  = items.IthomeReplyItem()
            article_resp['_id'] = resp_id
            article_resp['article_id'] = article_id
            article_resp['author'] = item_response.xpath(".//a[@class='response-header__person']/text()").get()
            article_resp['content'] = resp_content
            article_resp['publish_time'] = resp_date
            yield article_resp


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
