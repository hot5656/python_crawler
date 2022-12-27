# best_movies.py
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']

	# change user agent
    # start_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc', headers={
        	'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
		# add next page rule
		Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )


	# for scrappier 2.0
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='sc-80d4314-1 fbQftq']/h1/text()").get(),
            'year': response.xpath("//span[@class='sc-8c396aa2-2 itZqyK']/text()").get(),
            'duration': ''.join(response.xpath("//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt']/li[3]/text()").getall()),
            'genre': response.xpath("//div[@class='ipc-chip-list__scroller']/a/span/text()").getall(),
            'rating': response.xpath("//div[@data-testid='hero-rating-bar__aggregate-rating__score']/span[1]/text()").get(),
            'movie_url': response.url,
        }

