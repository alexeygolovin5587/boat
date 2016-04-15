# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoatItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    postID = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
    pass

month = {
	'January':'01',
	'February':'02',
	'March':'03',
	'April':'04',
	'May':'05',
	'June':'06',
	'July':'07',
	'August':'08',
	'September':'09',
	'October':'10',
	'November':'11',
	'December':'12'
}



