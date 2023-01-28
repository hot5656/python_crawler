from  scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor
# need put in front of "from twisted.internet import reactor"
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
from twisted.internet import reactor

# run by Twisted reactor
runner = CrawlerRunner(get_project_settings())
d = runner.crawl('articles')

d.addBoth(lambda _: reactor.stop())
reactor.run()

