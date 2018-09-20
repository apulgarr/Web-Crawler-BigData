import scrapy

class Spider(scrapy.Spider):
    name = 'anime'
    start_urls = []

    for page in range(1,120):
        start_urls.append('https://animeflv.net/browse?page=%d' % (page))


    def parse(self, response):
        for anime in response.css('article'):
            yield {
                    'title': anime.css('div.Description div.Title strong::text').extract_first(),
                    'description': anime.xpath('div/p[2]/text()').extract_first(),
            }
