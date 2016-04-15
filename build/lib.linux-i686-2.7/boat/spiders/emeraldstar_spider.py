

import scrapy
from items import BoatItem, month

class EmeraldstarSpider(scrapy.Spider):

	name = "emeraldstar"
	
	def __init__(self, start_urls, postIDArr, input_val):
		allowed_domains = ["www.emeraldstar.ie"]
		self.start_urls = start_urls
		self.postIDArr = postIDArr
		self.input_val = input_val
		self.index = 0;

	def parse(self, response):
		date = response.xpath('//td[@data-label="Start date"]/text()').extract();
		price = response.xpath('//td[contains(@data-label, "Price")]/text()').extract();
		for i in range(0, len(date)-1):
			item = BoatItem()
			temp_date = date[i].split(' ')
			year = self.input_val['date'].split('/')[2]
			temp_date = temp_date[1] + "/" + month[temp_date[2]] + "/" + year	

			item['date'] = temp_date					
			item['postID'] = self.postIDArr[self.index]
			item['price'] = price[i][1:]
			yield item

		self.index += 1


