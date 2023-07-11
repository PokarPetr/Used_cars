import scrapy
import time
import random
from used_cars.items import UsedCarsItem
from scrapy.loader import ItemLoader


class UcarsSpider(scrapy.Spider):
    name = "ucars"
    start_urls = ["https://www.autodiler.me/automobili/pretraga?pageNumber=1&formStyle=basic&sortBy=dateDesc"]

    def parse(self, response):
        for auto in response.css('div.oglasi-content-text div.oglasi-item-tekst.oglasi-item-tekst-automobili'):
            item = ItemLoader(item=UsedCarsItem(), selector=auto)
            item.add_value('resource', 'autodiler.me')
            item.add_css('make', 'a.oglasi-item-heading')
            item.add_css('model', 'a.oglasi-item-heading')
            item.add_css('distance', 'div.oglasi-item-tekst-tekst > ul li:nth-child(1)')
            item.add_css('year', 'div.oglasi-item-tekst-tekst > ul li:nth-child(2)')
            item.add_css('fuel', 'div.oglasi-item-tekst-tekst > ul li:nth-child(3)')
            item.add_css('price', 'div.cena p')
            item.add_css('location', 'div.oglasi-mesto p')

            yield item.load_item()

        next_page = response.css("a.ads-pagination__item-link::attr(href)").getall()[-1]

        if next_page is not None:
            time.sleep(
                random.choice([3.7, 1.9, 1.1, 2.8, 7.6, 4.8, 3.1, 6.1, 12.9, 3.3, 2.7, 1.8, 3.5, 2.9])
            )
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
