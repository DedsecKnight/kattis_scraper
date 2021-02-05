# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from kattis_scraper.items import KattisScraperItem

class KattisScraperPipeline:
    def open_spider(self, spider):
        self.problem_list = []
        

    def close_spider(self, spider):
        self.file = open('problem_list.txt', 'w', encoding='utf-8')
        for item in sorted(self.problem_list, key = lambda x : x['difficulty']):
            self.file.write(f"Problem {str(item['letter'])}" + '\n')
            self.file.write(str(item['name']) + '\n')
            self.file.write(str(item['problem_id']) + '\n')
            self.file.write(str(item['difficulty']) + '\n\n')
        self.file.close()

    def process_item(self, item, spider):
        if (isinstance(item, KattisScraperItem)):
            self.problem_list.append(item)  
        else: 
            self.file.write(str(item['notification']) + '\n')
        return item
