# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem
from  datetime import datetime
from shiyanlou.models import Respository,engine

class Resposity1Spider(scrapy.Spider):
	name = 'resposity1'
	@property
	def start_urls (self):
		url_templ = 'https://github.com/shiyanlou?tab=repositories&page={}'
		return (url_templ.format(i) for i in range(1,5))

	def parse(self, response):
		for Reposity in response.css('li.col-12'):
			item =ShiyanlouItem()
			item['name'] = Reposity.css('div.d-inline-block a::text').re_first('\s*([-\w]+)\s*')
			item['update_time'] = Reposity.css('relative-time::attr(datetime)').extract_first()
		
			yield item
        	
        	
