import scrapy
class GithubSpider(scrapy.Spider):
	name = 'github'
	@property
	def start_urls(self):
		url_tmpl = 'https://github.com/shiyanlou?tab=repositories&page={}'
		return (url_tmpl.format(i) for i in range(1,5))
		
		#for url in urls:
			#yield scrapy.Request(url=url,callback=self.parse)
	def parse(self,response):
		for course in response.css('li.d-block'):
			yield{
				'name':course.css('div.d-inline-block a::text').re_first('\s*(\w+)\s*'),
				'update_time':course.css('relative-time::attr(datetime)').extract_first()
}
