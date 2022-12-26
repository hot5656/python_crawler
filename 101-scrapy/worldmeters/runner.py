# runner.py for worldmeters.spiders.countries
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# set crawl code
from worldmeters.spiders.countries import CountriesSpider

# get configure
process = CrawlerProcess(settings=get_project_settings())
# set crawl entry
process.crawl(CountriesSpider)
process.start()