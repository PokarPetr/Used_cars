from scrapy.exceptions import DropItem

class UsedCarsPipeline:
    def process_item(self, item, spider):
        if not isinstance(item["price"], float):
            raise DropItem("Missing price value. Item excluded")
        if not isinstance(item["year"], int):
            raise DropItem("Missing price value. Item excluded")
        if not isinstance(item["distance"], float):
            raise DropItem("Missing price value. Item excluded")

        return item
