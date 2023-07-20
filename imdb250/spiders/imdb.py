import scrapy


class ImdSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/top/"]
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    def parse(self, response):
        for filmes in response.css('div.cli-children'):

            yield {
                'posicao':filmes.css('div.cli-title a h3::text').get().split('. ', 2)[0],
                'titulo': filmes.css('div.cli-title a h3::text').get().split('. ', 2)[1] ,
                'ano': filmes.css('div.cli-title-metadata span::text').extract()[0],
                'nota': filmes.css('span.ratingGroup--imdb-rating::text').get()

            }


        pass