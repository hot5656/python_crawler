import scrapy
from scrapy.shell import inspect_response

class CountriesSpider(scrapy.Spider):
  name = 'countries'
  allowed_domains = ['www.worldometers.info']
  # start_urls = ['https://www.worldometers.info/']
  start_urls = ['https://www.worldometers.info/world-population/population-by-country']

  def parse(self, response):
    countries = response.xpath("//td/a")
    for country in countries:
      name = country.xpath(".//text()").get()
      link = country.xpath(".//@href").get()

      # absolute url
      # absolute_url = f'https://www.worldometers.info{link}'
      # absolute_url = response.urljoin(link)
      # yield scrapy.Request(url=absolute_url)

      # relative url
      # add meta for callback parameter
      yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

  def parse_country(self, response, item=None):
    if item:
        # populate more `item` fields
        return item
    else:
        inspect_response(response, self)

    # inspect_response(response, self)
    # inspect_response(response, self)

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

