# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import datetime,timedelta
import gzip
import json
from ..items import GharchiveEvent

class GheventSpider(scrapy.Spider):
    name = 'ghevent'
    allowed_domains = ['data.gharchive.org']
    base_url = 'https://data.gharchive.org/'
    data_folder='/tmp/icollaborate/'
    custom_settings = {
        'ITEM_PIPELINES': {
            'gharchive.pipelines.GharchiveEventPipeline': 400
        }
    }
    def start_requests(self):
        os.makedirs(self.data_folder,exist_ok=True)
        period=self.settings.get('GHARCHIVEPERIOD')
        days=int(period.strip('D'))
        end=datetime.now().replace(minute=0,second=0,microsecond=0)
        start=end-timedelta(days=days)
        t=end
        while t>start:
            file=t.strftime('%Y-%m-%d-%H.json')
            url=self.base_url+file+'.gz'
            if not os.path.isfile(self.data_folder+file):
                req=scrapy.Request(url=url, callback=self.process_events)
                req.cb_kwargs['file']=file
                yield req
            t-=timedelta(hours=1)

    def process_events(self, response,file):
        data = gzip.decompress(response.body)
        with open(self.data_folder+file,'w') as f:
            f.write(data.decode())
        f.close()
        for l in data.decode().splitlines():
            event=GharchiveEvent()
            event['file']=self.data_folder+file
            event['data']=json.loads(l)
            yield event
        pass
