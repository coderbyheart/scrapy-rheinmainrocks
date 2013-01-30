from scrapy.item import Item, Field

class RheinmainrocksItem(Item):
    name= Field()
    subject=Field()
    location=Field()
    url=Field()
