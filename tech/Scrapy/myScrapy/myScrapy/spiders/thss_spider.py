import scrapy
from myScrapy.items import MyscrapyItem

class ThssSpider(scrapy.Spider):
    name = "thss"

    start_urls = ['https://www.thss.tsinghua.edu.cn/szdw/jsml.htm']

    # def start_requests(self):
    #     urls = ['https://music.163.com/#/song?id=1811721498']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        # page = response.url.split("/")[-2]
        # filename = f'thss-test-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')

        items = []
        institutions = response.css('div.group-title::text').getall()
        for i, institution in enumerate(institutions):
            teachers = response.css('div.group-people')[i].css('a::text').getall()
            for teacher in teachers:
                item = MyscrapyItem()
                item['name'] = teacher
                item['institution'] = institution
                items.append(item)

        return items
