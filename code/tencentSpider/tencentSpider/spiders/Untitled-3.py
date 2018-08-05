import scrapy


class RenrenSpider(scrapy.Splider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = []

    def start_requires(self):
        url = 'http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(url=url, formdata={ 'email': 'xxxxxx@163.com',  'password': 'alarmchime'}, callback=self.parse_page)
    
    def parse_page(self, response):
        with open('mo.html', 'w') as f:
            f.write(response.body)