import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    # start_urls = ['http://worldpopulationreview.com/']
    start_urls = ['https://worldpopulationreview.com/country-rankings/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//tbody/tr")
        for row in rows:
            name = row.xpath("./td[1]/a/text()").get()
            debt_rate = row.xpath("./td[2]/text()").get()

            yield {
                'country_name' : name,
                'debt_rate' : debt_rate
            }
