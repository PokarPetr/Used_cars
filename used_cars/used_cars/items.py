import scrapy
import re
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags, remove_tags_with_content

def remove_b(value):
    return remove_tags_with_content(value, which_ones=('b',))

def ext_fuel(value):
    try:
        return value.split()[1]
    except IndexError:
        return "-"

def ext_price(value):
    try:
        return value.split()[0]
    except IndexError:
        return "-"

def try_float(value):
    try:
        return float(value)
    except ValueError:
        return value

def try_int(value):
    try:
        return int(value)
    except ValueError:
        return value

def extract_make(value):
    try:
        return value.split('-')[0]
    except IndexError:
        return '-'

def extract_model(value):
    try:
        return value.split('-')[1]
    except IndexError:
        return '-'



class UsedCarsItem(scrapy.Item):
    resource = scrapy.Field()
    make = scrapy.Field(
        input_processor=MapCompose(remove_tags, extract_make, str.strip),
        output_processor=TakeFirst()
    )
    model = scrapy.Field(
        input_processor=MapCompose(remove_tags, extract_model, str.strip),
        output_processor=TakeFirst()
    )
    distance = scrapy.Field(
        input_processor=MapCompose(remove_b, remove_tags, lambda value: re.findall(r'\d+', value), try_float),
        output_processor=TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(remove_b, remove_tags, lambda value: re.findall(r'\d{4}', value), try_int),
        output_processor=TakeFirst()
    )
    fuel = scrapy.Field(
        input_processor=MapCompose(remove_b, remove_tags, ext_fuel),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, ext_price, try_float),
        output_processor=TakeFirst()
    )
    location = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )


