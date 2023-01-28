import scrapy
# from ..items import as items
import ithome2.items as items


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['ithelp.ithome.com.tw']

    def start_requests(self):
        for page in range (1,2):
            yield scrapy.Request(url=f"https://ithelp.ithome.com.tw/articles?tab=tech&page={page}", callback=self.parse)

    def parse(self, response):
        # with open('ithome.html', 'wb') as f:
        #     f.write(response.body)

        articles = response.xpath("//div[@class='board tabs-content']/div[@class='qa-list']")
        for article in articles:
            article_url = article.xpath(".//a[@class='qa-list__title-link']/@href").get()
            yield response.follow(article_url, callback=self.article_parse)

    def article_parse(self, response):
        article_head = response.xpath("//div[@class='qa-header']")
        content = ''.join(response.xpath("//div[@class='markdown__style']/descendant::text()").getall())
        content = self.content_alignment(content)
        tags = article_head.xpath(".//a[contains(@class,'tag qa-header__tagList')]/text()").getall()

        # article = {
        #     'url': response.url,
        #     'author': article_head.xpath(".//a[@class='qa-header__info-person']/text()").get(),
        #     'publish_time': article_head.xpath(".//a[@class='qa-header__info-time']/@title").get(),
        #     'view_count': article_head.xpath(".//span[@class='qa-header__info-view']/text()").get().split(" ")[0],
        #     'title': article_head.xpath("normalize-space(.//h2[@class='qa-header__title']/text())").get(),
        #     'tags': ','.join(tags),
        #     'content': content,
        # }

        article = items.IthomeArticleItem()
        article['url'] =  response.url
        article['author'] = article_head.xpath(".//a[@class='qa-header__info-person']/text()").get()
        article['publish_time'] = article_head.xpath(".//a[@class='qa-header__info-time']/@title").get()
        article['view_count'] = int(article_head.xpath(".//span[@class='qa-header__info-view']/text()").get().split(" ")[0])
        article['title'] = article_head.xpath("normalize-space(.//h2[@class='qa-header__title']/text())").get()
        article['tags'] = ','.join(tags)
        article['content'] = content
        yield article

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
