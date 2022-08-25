import scrapy
import time

from scrapy.http import Request
from scrapy.spiders import CrawlSpider 

from .itemloader import SmartphonesItemLoader 
from darwin_scrapers.items import SmartphonesItem


class SmartphonesSpider(CrawlSpider):

    name = "smartphones"

    # scraped links
    main_page_url = "https://darwin.md/telefoane/smartphone" 
    query_url = "https://darwin.md/telefoane/smartphone?page={}"

    def start_requests(self):
        return [Request(
            url=self.main_page_url,
            callback=self.generate_requests,
            meta={
                'cookiejar': time.time()
            },
            dont_filter=True
        )]

    def generate_requests(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        number_of_pages = int(response.xpath(
            "//li[@class='page-item truncate']/a/text()"
        ).extract_first())

        return [Request(
            url=self.query_url.format(page_number),
            callback=self.parse_item,
            meta={
                'cookiejar': time.time()
            },
            dont_filter=True
        ) for page_number in range(1, number_of_pages+1)]

    def parse_item(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        products = response.xpath(
            ("//section[@class='products']"
            "/div[@class='container']"
            "/div[@class='item-products ']"
            "/div[@class='row rowlast']"
            "/div[@class='col-6 col-md-4 col-lg-3 night-mode']")
        )

        for product in products:
            loader = SmartphonesItemLoader(
                item=SmartphonesItem(),
                selector=product,
                response=response
            ) 
            yield loader.extract()

