# runner.py for imdb.spiders.best_movies
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# set crawl code
from imdb.spiders.best_movies import BestMoviesSpider

# get configure
process = CrawlerProcess(settings=get_project_settings())
# set crawl entry
process.crawl(BestMoviesSpider)
process.start()