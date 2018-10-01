import scrapy
from getData import Data


#response.xpath("//a/@href").extract()
class SiataSpider(scrapy.Spider):
    name = 'siataSpider'
    allowed_domain = 'siata.gov.co'
    url = 'https://siata.gov.co/descarga_siata//application/assets/assets-siata/downloads/HgMfhJBrrVvecoZ2TbTeJg/'
    start_urls = [url]

    def parse(self, response):
        url = 'https://siata.gov.co/descarga_siata//application/assets/assets-siata/downloads/HgMfhJBrrVvecoZ2TbTeJg/'
        urls = response.xpath('//a/@href').extract()[5:]
        instance = Data(response.url, urls)
        instance.get_item()

