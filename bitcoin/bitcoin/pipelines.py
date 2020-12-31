# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class BitcoinPipeline:
    collection_name = "Data"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client["Bitcoin"]

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
    
