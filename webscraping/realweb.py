from cgitb import text
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
print("Enter the skills you are not familiar with")
unfamiliar_skill = input('-> ')
print(f"Filtering out : {unfamiliar_skill}")
job = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
#print(jobs)
for jobs in job:
    published_date = jobs.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:

        company_name  = jobs.find('h3', class_ = "joblist-comp-name").text.replace(' ', '')
        skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ', '')
        more_info = jobs.header.h2.a['href']
        print(f"Company Name : {company_name.strip()}")
        print(f"Required Skills : {skills.strip()}")
        print(f"More Info : {more_info}")
        print('')

