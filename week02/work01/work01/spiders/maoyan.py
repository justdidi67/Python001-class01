# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.selector import Selector
from work01.items import Work01Item
import json


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    #解析函数    
    def parse(self, response):
        for movie in Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]:
            item = Work01Item()
            item['movie_name'] = movie.xpath('./div[1]/span[1]/text()').get()
            item['movie_type'] = movie.xpath('./div[2]/text()[2]').get().strip()
            item['showtime'] = movie.xpath('./div[4]/text()[2]').get().strip()
            print(item['movie_name'],item['movie_type'],item['showtime'])
            yield item