# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas


class Work02Pipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        showtime = item['showtime']
        output = [movie_name, movie_type, showtime]

        movies = pandas.DataFrame(output)
        movies.to_csv('./work02.csv',mode='a+',encoding='utf_8_sig')
        return item
