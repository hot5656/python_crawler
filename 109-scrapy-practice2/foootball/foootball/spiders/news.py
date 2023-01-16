import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['foootball.cc']
    start_urls = ['https://foootball.cc/']
    index = 0
    MAX_NEWS = 75

    def parse(self, response):
        news = response.xpath("(//h2[@class='h2-title topic-line-four'])[2]/following::div/div[@class='row']")
        for new in news:
            if new.xpath(".//h4//a/text()").get()== None or (self.index >= self.MAX_NEWS):
                break

            self.index +=1
            image_url_str = new.xpath(".//div[@class='containerimg']/a/@style").get();
            image_url = image_url_str.split('(')[-1].split(')')[0];
            yield {
                'title' : new.xpath(".//h4//a/text()").get(),
                'artical_url': new.xpath(".//h4/a/@href").get(),
                'image_url': image_url,
                'date': new.xpath("normalize-space(.//div[@class='mainnews-info-small']/span/text())").get(),
                'index': self.index
            }

        next_page =  response.xpath("//a[@rel='next']/@href").get()
        if next_page or self.index < self.MAX_NEWS:
            print("=========================")
            print("--"+next_page+"--")
            # print(response.urljoin(next_page))
            yield scrapy.Request(url=next_page, callback=self.parse)


        # (//h2[@class='h2-title topic-line-four'])[2]/following::div/div[@class='row']
