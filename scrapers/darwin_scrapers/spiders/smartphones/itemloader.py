from scrapy.loader import ItemLoader

class SmartphonesItemLoader(ItemLoader):

    def extract(self):

        self.add_css("name", "h3.title a::text")
        self.add_css("price", "span.price-new b::text")
        self.add_css("image", "img.card-image::attr(src)")

        return self.load_item()