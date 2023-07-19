import scrapy


class ImdSpider(scrapy.Spider):
    name = "imd"
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield {
                'titulo': filmes.css('.titleColumn a::text'),
                'ano': filmes.css('.secondaryInfo ::text'),
                'nota': response.css('strong::text')
            }


        pass
