# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import DictItem
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class AnjukeItem(scrapy.Item):
    house_id = scrapy.Field()  # 房屋id
    title = scrapy.Field()  # 楼盘名称
    guarantee_info = scrapy.Field()  # 安选验真信息
    link = scrapy.Field()  # 链接
    area = scrapy.Field()  # 面积
    house_type = scrapy.Field()  # 户型
    floor_info = scrapy.Field()  # 楼层信息
    build_time_info = scrapy.Field()  # 建造时间信息
    broker_name = scrapy.Field()  # 经纪人姓名
    address = scrapy.Field()  # 地址
    locate_a = scrapy.Field()  # 一级区域信息 eg：浦东
    locate_b = scrapy.Field()  # 二级区域信息 eg：张江
    tags = scrapy.Field()  # 地址
    price = scrapy.Field(serializer=float)  # 价格
    unit_price = scrapy.Field(serializer=float)  # 每平米价格
    get_time = scrapy.Field(serializer=float)  # 数据获取时间



base = declarative_base()


class AnjukeBean(base):
    __tablename__ = 'anjuke_sale_data'
    house_id = Column(String(20), primary_key=True)  # 房屋id
    title = Column(String(20))  # 楼盘名称
    guarantee_info = Column(String(20))  # 安选验真信息
    link = Column(String(20), nullable=True)  # 链接
    area = Column(String(20))  # 面积
    house_type = Column(String(20))  # 户型
    floor_info = Column(String(20))  # 楼层信息
    build_time_info = Column(Integer())  # 建造时间信息
    broker_name = Column(String(20))  # 经纪人姓名
    address = Column(String(20))  # 地址
    locate_a = Column(String(20))  # 一级区域信息 eg：浦东
    locate_b = Column(String(20))  # 二级区域信息 eg：张江
    tags = Column(String(20))  # 地址
    price = Column(Integer())  # 价格
    unit_price = Column(Integer())  # 每平米价格
    get_time = Column(String(20))  # 数据获取时间

    def __str__(self):
        return 'id:%s-title:%s-area:%s-address:%s' % (self.house_id, self.title, self.area, self.address)
