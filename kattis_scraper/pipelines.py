# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from kattis_scraper.items import ContestID
from itemadapter import ItemAdapter
from kattis_scraper.items import KattisScraperItem
from kattis_scraper.templates.java import java_template
from kattis_scraper.templates.cpp import cpp_template
import os

class KattisScraperPipeline:
    # Specify where you want your submission file to be generated
    KATTIS_PATH = r"kattis/contests"

    # Specify the language for your submission file (currently supports cpp and java)
    FILE_TYPE = "cpp"

    # Specify whether you want to generate submission file
    GENERATE_SUBMISSION_FILE = True

    def open_spider(self, spider):
        self.problem_list = []
        self.problem_id = ""

    # Generate template based on problem name
    def generate_template(self, problem_letter):
        if (self.FILE_TYPE == "java"): return java_template(problem_letter)
        if (self.FILE_TYPE == "cpp"): return cpp_template(problem_letter)
        return []

    # Create submission file
    def create_file(self, submission_path, problem_letter):
        submission_file = open(f"{submission_path}/{problem_letter}.{self.FILE_TYPE}", "x")
        template = self.generate_template(problem_letter)
        for line in template:
            submission_file.write(line)
            submission_file.write('\n')
        submission_file.close()

    def close_spider(self, spider):
        # problem_list.txt will store problem name, letter, and difficulty
        self.file = open('problem_list.txt', 'w', encoding='utf-8')
        submission_path = None

        # Create directory for current contest to store submission_file
        if (self.GENERATE_SUBMISSION_FILE):
            submission_path = os.path.join(self.KATTIS_PATH, self.problem_id)
            os.makedirs(submission_path)

        for item in sorted(self.problem_list, key = lambda x : x['difficulty']):
            # Write problem to problem_list.txt
            self.file.write(f"Problem {str(item['letter'])}" + '\n')
            self.file.write(str(item['name']) + '\n')
            self.file.write(str(item['difficulty']) + '\n\n')

            # Generate submission file for that problem (if necessary)
            if (self.GENERATE_SUBMISSION_FILE): 
                self.create_file(submission_path, str(item['letter']))
                
        self.file.close()

    def process_item(self, item, spider):
        if (isinstance(item, ContestID)): 
            # Set contest ID
            self.problem_id = str(item['cid'])
        elif (isinstance(item, KattisScraperItem)):
            # Add problem to problem-list
            self.problem_list.append(item)  
        else: 
            # Print out notification
            self.file.write(str(item['notification']) + '\n')
        return item
