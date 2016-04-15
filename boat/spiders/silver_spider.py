import scrapy

import mechanize
from items import BoatItem, month
import json

class Silver(scrapy.Spider):
	name = 'sliver'
	allowed_domains = ['www.silverlinecruisers.com']

	def __init__(self, result):
		
		self.result = result
		self.index = 0;

	def start_requests(self):
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.set_handle_equiv(False)

		for key in self.result[0]:
			yield scrapy.Request(url = 'http://silverlinecruisers.com/slc/wp-admin/admin-ajax.php',
				callback = self.parse,
				method = 'POST',
				headers = {
					"cache-control":"no-cache",
					"cookie":"pll_language=en; woocommerce_recently_viewed=7909",
					"accept-language":"en-US,en;q=0.8",
					"accept-encoding":"gzip, deflate",
					"referer":key,
					"dnt":"1",
					"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
					"user-agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; AskTB5.6)",
					"x-requested-with":"XMLHttpRequest",
					"origin":"http//silverlinecruisers.com",
					"accept":"text/html, */*; q=0.01"
				},
				body = "action=wc_bookings_calculate_costs&form=" + self.result[0][key],				
			)


	def pcm(self, error):
		print error
	def parse(self, response):
		print "-"*10
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
