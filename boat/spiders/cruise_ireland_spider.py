
import scrapy
from items import BoatItem, month

def is_number(var):
    try:
        var = int(var)
        return var
    except Exception:
        return False

class CruiseIreland(scrapy.Spider):

	name = "cIreland"
	
	def __init__(self, start_urls, postIDArr, input_val):
		allowed_domains = ["www.cruise-ireland.com"]
		self.start_urls = start_urls
		self.postIDArr = postIDArr
		self.input_val = input_val
		self.index = 0;

	def parse(self, response):
			
		for table in response.xpath('//table[@id="boat-options"]'):
			for tr in table.xpath('.//tr'):
				price = tr.xpath('.//td[@class="price"]/text()').extract()
				if len(price):
					item = BoatItem()

					date = tr.xpath('.//td[2]/text()').extract()
					
					temp = date[0].split('<br>')[0]
					temp_date = temp.split(' ')[1:]
					temp_date[0] = temp_date[0][:-2]
					temp_date[1] = month[temp_date[1]]
										
					item['date'] = '/'.join(temp_date)					

					item['postID'] = self.postIDArr[self.index]
					item['price'] = price[0]
					yield item
		self.index += 1


