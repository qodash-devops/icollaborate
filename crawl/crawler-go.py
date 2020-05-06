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
    def search(self,description,loglevel="INFO"):
        '''
        :param description:  string
        :param loglevel: INFO | DEBUG | WARNING | ERROR
        :return:
        '''
        settings = Settings()
        os.environ['SCRAPY_SETTINGS_MODULE'] = 'edgar.settings'
        settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
        settings.setmodule(settings_module_path, priority='project')
        settings = get_project_settings()

        settings.set("LOG_LEVEL", loglevel)
        process = CrawlerProcess(settings)
        process.crawl("github")
        process.start()


if __name__ == '__main__':
    Fire(CrawlerGo)
