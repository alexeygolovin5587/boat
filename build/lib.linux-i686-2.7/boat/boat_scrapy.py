
import sys
import json
from scrapy.utils.project import get_project_settings

from scrapy.crawler import CrawlerProcess
from spiders.cruise_ireland_spider import CruiseIreland
from spiders.emeraldstar_spider import EmeraldstarSpider
from spiders.silver_spider import Silver

from urlfilters import *

# scrapy data based on the list of given urls
def scrapy_data(cralwer, res, domain, input_val):	
	if domain == "cruise-ireland.com":	
		crawler.crawl(CruiseIreland, start_urls = res[0], postIDArr=res[1], input_val=input_val)
	elif domain == "www.emeraldstar.ie":
		crawler.crawl(EmeraldstarSpider, start_urls = res[0], postIDArr=res[1], input_val=input_val)
	else:
		pass



if __name__ == '__main__':
	# get data from shell	
	input_val = json.loads(sys.argv[1])

	crawler = CrawlerProcess(get_project_settings())
#cruise_ireland url
	res = gen_cruise_ireland_urls(input_val)
	scrapy_data(crawler, res, "cruise-ireland.com", input_val)
#emeraldstar url
	res = gen_emeraldstar_urls(input_val)
	scrapy_data(crawler, res, "www.emeraldstar.ie", input_val)

#silver url
#	res = gen_silver_urls(input_val)
#	crawler.crawl(Silver, result = res)
	crawler.start()
	#
	

