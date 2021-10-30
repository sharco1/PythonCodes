import scrapy


class mobileSpider(scrapy.Spider):
    name = 'mobiles'
    allowed_domains = ['mobile.ir/phones/prices.aspx']
    start_urls = ['https://www.mobile.ir/phones/prices.aspx']

    def parse(self, response):
        for mobile in response.xpath('//*[@id="price_table"]'):
            yield {
                'Mobile_price':mobile.xpath('./tbody/tr/td[3]/a/text()').get(),
                'Mobile_name': mobile.xpath('./tbody/tr/td[2]/a/text()').get(),

            }