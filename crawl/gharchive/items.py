from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config

import scrapy


class GharchiveEvent(scrapy.Item):
    # define the fields for your item here like:
    file = scrapy.Field()
    data = scrapy.Field()
    pass



