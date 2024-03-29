from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# scrapy run crawler Process
process = CrawlerProcess(get_project_settings())
process.crawl('articles')
process.start()