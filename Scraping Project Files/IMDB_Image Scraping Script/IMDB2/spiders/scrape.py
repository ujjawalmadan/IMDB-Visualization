# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import re
import pandas as pd

class ScrapeSpider(scrapy.Spider):
    name = 'scrape'
    allowed_domains = ['www.imdb.com']
    start_urls = ["https://www.imdb.com/title/tt4460418/"]

    script = '''
    	function main(splash, args)
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
			return splash:html()
		end
	'''

    Codes = pd.read_csv('./Images_Codes.csv').x
    
    def start_requests(self):
        start = 0
        for i in range(0, 10710):
            link = 'https://www.imdb.com/title/' + str(self.Codes[i])
            yield scrapy.Request(url = link, callback = self.parse, meta={'Code': str(self.Codes[i])})
         
    def parse(self, response):
        #Code = "tt" + re.findall(r'\d{1,10}', response.url)[0]  
        image_link = "https://www.imdb.com" + response.xpath("//div[@class='poster']/a/@href").get()
        yield SplashRequest(url = image_link, callback = self.parse_image, endpoint = "execute", args= {'lua_source': self.script, 'timeout': '90'}, meta = {'Code': response.request.meta['Code']})
    
    def parse_image(self, response):
        yield{'Code': response.request.meta['Code'],
            'Image': response.xpath("(//img[@class='pswp__img'])[1]/@src").get()}
