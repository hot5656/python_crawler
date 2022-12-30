import scrapy
from scrapy import FormRequest
import open_library


class OpenlibaryLoginSpider(scrapy.Spider):
    name = 'openlibrary_login2'
    allowed_domains = ['archive.org']
    start_urls = ['https://archive.org/account/login']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            # formxpath also need
            formxpath='//form[@class="iaform login-form"]',
            formdata = {
                'username': open_library.username,
                'password': open_library.password,
                # 'remember': response.xpath("//input[@name='remember']/@value").get(),
                # 'referer': response.xpath("//input[@name='referer']/@value").get(),
                # 'login': response.xpath("//input[@name='login']/@value").get(),
                'login': 'true',
                'remember': 'true',
                'referer': 'https://archive.org/',
                'submit-to-login': 'Log in'
            },
            callback = self.after_login
        )

    def after_login(self, response):
        print("=================")
        if  response.xpath("//input[@type='password']").get():
            print('login failed...')
        else:
            print('logged in...')
