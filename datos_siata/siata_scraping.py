import scrapy
from getData import Data


#response.xpath("//a/@href").extract()
class SiataSpider(scrapy.Spider):
    name = 'siataSpider'
    allowed_domain = 'siata.gov.co'
    url = 'https://siata.gov.co/descarga_siata/////application/assets/assets-siata/downloads/XwBNdeiOtVsV26eZhOybvw/'
    start_urls = [url]

    def parse(self, response):
        urls = response.xpath('//a/@href').extract()[5:]
        instance = Data(response.url, urls)
        instance.get_item()

