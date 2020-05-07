# -*- coding: utf-8 -*-
import scrapy
from ..graph import get_repo_url_missing_readme,Repo
import json
class ReposSpider(scrapy.Spider):
    name = 'repos'
    allowed_domains = ['github.com']

    def start_requests(self):
        urls=get_repo_url_missing_readme()
        for url in urls[:50]:
            req=scrapy.Request(url,self.parse_desc)
            yield req

    def parse_desc(self,response):
        d=json.loads(response.body)
        desc=d['description']
        html_url = response.url.replace('api.', '').replace('repos/', '')
        readme_url = html_url + '/blob/master/README.md'
        req = scrapy.Request(readme_url, self.parse_readme)
        req.meta['desc'] = desc
        req.meta['repo_url']=response.url
        yield req



    def parse_readme(self, response):
        desc = response.meta['desc']
        readme=response.xpath('//div[@id="readme"]').get()
        repo_url=response.meta['repo_url']

        #Update the node info in the database
        node=Repo.nodes.filter(url=repo_url).all().pop()
        node.description=desc
        node.readme=readme
        node.save()

