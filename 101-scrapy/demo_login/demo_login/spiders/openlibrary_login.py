import scrapy
from scrapy import FormRequest
import open_library


class OpenlibaryLoginSpider(scrapy.Spider):
    name = 'openlibrary_login'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/account/login']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            formid='register',
            formdata = {
                'username': open_library.username,
                'password': open_library.password,
                'redirect': '/',
                'debug_token': '',
                'login': '登录'
            },
            callback = self.after_login
        )

    def after_login(self, response):
        print("=================")
        if  response.xpath("//input[@type='password']").get():
            print('login failed...')
        else:
            print('logged in...')
