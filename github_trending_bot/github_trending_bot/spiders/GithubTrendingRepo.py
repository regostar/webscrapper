# -*- coding: utf-8 -*-
import scrapy


class GithubtrendingrepoSpider(scrapy.Spider):
    name = 'GithubTrendingRepo'
    allowed_domains = ['github.com/trending/']
    start_urls = ['http://github.com/trending//']

    def parse(self, response):
        print("%s : %s : %s" % (response.status, response.url, response.text))
