# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class CoursesSpider(scrapy.Spider):
	name = 'courses'
    	#allowed_domains = ['shiyanlou.com']
	@property
	def start_urls(self):
	    url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
	    return (url_tmpl.format(i) for i in range(1,5))
	def parse(self, response):
	    for Repository in response.css('li.col-12'):
		item = ShiyanlouItem({
		'name':Repository.css('a::text').extract_first().strip(),
		'update_time':Repository.css('relative-time::attr(datetime)').extract_first()})
            	yield item

