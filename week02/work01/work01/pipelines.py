# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymysql
from traceback import format_exc
from itemadapter import ItemAdapter


class Work01Pipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

    def __init__(self, host, user, password, db, table, port=3306):
        self.db = db
        self.table = table
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('DB_HOST'),
            user=crawler.settings.get('DB_USER'),
            password=crawler.settings.get('DB_PWD'),
            db=crawler.settings.get('DB'),
            table=crawler.settings.get('TABLE')
        )

    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        showtime = item['showtime']
        sql = 'INSERT INTO scrapy.maoyanmovies(`movie_name`,`movie_type`,`showtime`) VALUES (\''+movie_name+'\',\''+movie_type+'\',\''+showtime+'\');'
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except:
            self.conn.rollback()
            print('save to db failed except:%s', format_exc())
        finally:
            cur.close()
        return item

    def close_spider(self, spider):
        self.conn.close()
