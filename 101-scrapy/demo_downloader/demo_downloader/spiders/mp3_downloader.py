import scrapy

class Mp3DownloaderSpider(scrapy.Spider):
    name = 'mp3_downloader'
    allowed_domains = ['ftp.icm.edu.pl']
    start_urls = ['https://ftp.icm.edu.pl/packages/mp3/59/']

    def parse(self, response):
        # //following::tr[4]/td[2]/a[not(contains(@href,'jpg'))] - also ok
        for link in response.xpath("//following::tr[4]/td[2]/a[contains(@href,'mp3')]"):
            relative_url = link.xpath(".//@href").get()
            absolute_url = response.urljoin(relative_url)
            print("==============")
            print(f"absolute_url : {absolute_url}")
            yield {
                'Title':  relative_url,
                'file_urls': [absolute_url]
            }
