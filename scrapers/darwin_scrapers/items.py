import scrapy
from itemloaders.processors import TakeFirst, Identity

class SmartphonesItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst()
    )
    image = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst()
    )

