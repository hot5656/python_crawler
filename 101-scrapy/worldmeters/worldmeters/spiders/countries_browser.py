import scrapy
from scrapy.utils.response import open_in_browser

class CountriesSpider(scrapy.Spider):
  name = 'countries_browser'
  allowed_domains = ['www.worldometers.info']
  # start_urls = ['https://www.worldometers.info/']
  start_urls = ['https://www.worldometers.info/world-population/population-by-country']

  def parse(self, response):
    # countries = response.xpath("//td/a")
    # for country in countries:
    #   name = country.xpath(".//text()").get()
    #   link = country.xpath(".//@href").get()

      # absolute url
      # absolute_url = f'https://www.worldometers.info{link}'
      # absolute_url = response.urljoin(link)
      # yield scrapy.Request(url=absolute_url)

      # relative url
      # add meta for callback parameter
    yield response.follow(url="https://www.worldometers.info/world-population/china-population/", callback=self.parse_country, meta={'country_name': 'China'})

  def parse_country(self, response):
    open_in_browser(response)

    # add meta for callback parameter
    # name = response.request.meta['country_name']
    # rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
    # for row in rows:
    #   year = row.xpath("./td[1]/text()").get()
    #   population = row.xpath("./td[2]/strong/text()").get()
    #   yield {
    #     'country_name' : name,
    #     'year' : year,
    #     'population': population
    #   }
