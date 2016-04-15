# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BoatPipeline(object):
	def __init__(self):
		self.file = open('items.jl', 'wb')
		self.result = []

	def process_item(self, item, spider):
		self.result.append(dict(item))
		return item
	
	def open_spider(self, spider):
		pass	

	def close_spider(self, spider):
		print json.dumps(self.result) + ','
		#self.file.write(josn.dumps(self.result))


