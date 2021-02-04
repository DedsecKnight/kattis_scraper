# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from kattis_scraper.items import KattisScraperItem

class KattisScraperPipeline:
    def open_spider(self, spider):
        self.file = open('problem_list.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if (isinstance(item, KattisScraperItem)):
            self.file.write(str(item['name']) + '\n')
            self.file.write(str(item['problem_id']) + '\n')
            self.file.write(str(item['difficulty']) + '\n\n')
        else: 
            self.file.write(str(item['notification']) + '\n')
        return item
