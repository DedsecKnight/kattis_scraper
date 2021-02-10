from kattis_scraper.items import KattisScraperItem, AlertItem, ContestID
from scrapy import Request, Spider
from bs4 import BeautifulSoup

class KattisSpider(Spider):
    name = "kattis"

    BASE_URL = 'https://open.kattis.com'
    out_file = None

    def get_problemset(self, contest_id):
        return f'{self.BASE_URL}/contests/{contest_id}/problems'

    def start_requests(self):
        contest_id = input('Enter contest id: ')

        urls = [self.get_problemset(contest_id)]
        for url in urls: 
            yield Request(url=url, callback=self.contest_parse, cb_kwargs=dict(
                contest_id = contest_id
            ))
        
    def contest_parse(self, response, contest_id):
        # Check if contest ID is valid
        problem_page = response.css('.page-content, .boxed, .clearfix').getall()
        if (len(problem_page) <= 2): 
            yield AlertItem(notification="Invalid contest ID")
            return
        
        # Send contest ID to pipeline
        yield ContestID(cid=contest_id)
        
        # Check if problemset can be accessed
        soup = BeautifulSoup(markup = problem_page[2], features = 'lxml')
        soup = soup.find('table', { 'id' : 'contest_problem_list' })
        if (not soup):
            yield AlertItem(notification="Contest hasn't started yet")
            return 

        soup = soup.find('tbody')

        # Process each problem in the problemset
        problem_list = soup.find_all('tr')
        for problem in problem_list:
            problem_letter = problem.find('th').get_text()
            problem_name = problem.find('td').find('a').get_text()
            problem_link = problem.find('td').find('a')['href']
            start_idx = problem_link.index('/problems')
            problem_link = self.BASE_URL + problem_link[start_idx:]
            yield Request(url = problem_link, callback = self.problem_parse, cb_kwargs=dict(
                problem_name = problem_name, 
                problem_letter = problem_letter
            ))
    
    def problem_parse(self, response, problem_name, problem_letter):
        soup = BeautifulSoup(markup = response.text, features='lxml')
        sidebar = soup.find('div', class_='problem-sidebar sidebar-info').find_all('div', class_='sidebar-info')[1]
        
        # Get problem ID and difficulty
        problem_info = sidebar.find_all('p')
        difficulty = problem_info[3].get_text()

        yield KattisScraperItem(name=problem_name, letter=problem_letter, difficulty=difficulty)

