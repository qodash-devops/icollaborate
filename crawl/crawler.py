from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings

from fire import Fire
import os
import colorlog
import logging

#logging
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s[%(asctime)s - %(levelname)s]:%(message)s'))
logger = colorlog.getLogger('Crawler-Startup')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class CrawlerGo:
    def start(self,period='10D',spider='ghevent',loglevel="INFO"):
        '''

        :param period: crawling period for events
        :param spider: spider name
        :param loglevel: INFO , DEBUG ...
        :return:
        '''
        settings = Settings()
        settings_module_path = 'gharchive.settings'
        settings.setmodule(settings_module_path, priority='project')
        settings = get_project_settings()
        settings.set("LOG_LEVEL", loglevel)
        settings.set("GHARCHIVEPERIOD",period)
        process = CrawlerProcess(settings)
        process.crawl(spider)
        process.start()


if __name__ == '__main__':
    Fire(CrawlerGo)
