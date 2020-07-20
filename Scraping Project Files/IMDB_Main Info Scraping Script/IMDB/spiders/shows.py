# -*- coding: utf-8 -*-
import scrapy
import re
import pandas as pd

class ShowsSpider(scrapy.Spider):
    name = 'shows'
    allowed_domains = ['www.imdb.com']
    start_urls = ["https://www.imdb.com/title/tt9748726/"]
    
    #Codes = pd.read_csv('E:/scrapy/files/IMDB_Codes.csv').x
    Codes = pd.read_csv('./Main_Info_Codes.csv').x

    def start_requests(self):
        for i in range(0, 2021):#70580, 2021
            link = 'https://www.imdb.com/title/' + str(self.Codes[i])
            yield scrapy.Request(url = link, callback = self.parse, meta={'Code': str(self.Codes[i])})

    def parse(self, response):
        Title = response.xpath("//div[@class='title_wrapper']/h1/text()").get('').strip()
        RunTime = response.xpath("//time/text()").get('').strip()
        Plot = response.xpath("//div[@class='plot_summary ']/div[1]/text()").get('').strip()
        Episode_Aired = response.xpath ("//div[@class='subtext']/a[@title='See more release dates']/text()").get('').strip('\n').strip('Episode aired ')
        Total_Ratings = response.xpath("//span[@class='small']/text()").get('')

        image_link = "https://www.imdb.com" + response.xpath("//div[@class='poster']/a/@href").get('')    
        yield scrapy.Request(url = image_link, callback=self.parse_image, meta = {'Title': Title, 'RunTime': RunTime, 'Plot': Plot, 'Episode Aired': Episode_Aired, 'Total Ratings': Total_Ratings, 'Code': response.request.meta['Code'] })
    
    def parse_image(self, response):
        yield{
            'Title': response.request.meta['Title'],
            'RunTime': response.request.meta['RunTime'],
            'Plot': response.request.meta['Plot'],
            'Episode_Aired': response.request.meta['Episode Aired'],
            'Actual_Link': response.xpath("//meta[@itemprop='image'][1]/@content").get(''),
            'Total_Ratings':  response.request.meta['Total Ratings'],
            'Code': response.request.meta['Code']
        }




