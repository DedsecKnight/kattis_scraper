# Kattis Scraper

This is a web crawler bot created to show the difficulties of problems in Kattis contest 

## Usage instructions:

### Required Installation
Install Python 3.9 <br />
Install BeautifulSoup and Scrapy for Python <br />

### Template-generating instructions
Go to pipelines.py <br />
Set KATTIS_PATH to the path where you want to store your submissions <br />
Set FILE_TYPE to your preferred programming language (currently supports C++ and Java) <br />
Sample templates are included in this repository <br />

### Execution instructions
Cd into this directory <br />
Run "scrapy crawl kattis" <br />
When prompted, type in the contest ID, which can be found after "/contests" in the contest URL <br />
Information about the problemset will be exported to problem_list.txt <br />
