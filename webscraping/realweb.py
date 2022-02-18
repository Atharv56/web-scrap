from cgitb import text
from bs4 import BeautifulSoup
import requests
import time
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    print("Enter the skills you are not familiar with")
    unfamiliar_skill = input('-> ')
    print(f"Filtering out : {unfamiliar_skill}")
    job = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    #print(jobs)
    for index, jobs in enumerate(job):
        published_date = jobs.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:

            company_name  = jobs.find('h3', class_ = "joblist-comp-name").text.replace(' ', '')
            skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = jobs.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'/Users/atharvsalian/Desktop/Github/web-scrap/web-scrap/webscraping/posts/{index}.txt', 'w') as f:

                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Required Skills : {skills.strip()} \n")
                    f.write(f"More Info : {more_info} \n")
                print(f'File Created : {index}')
                    

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting for {time_wait} minutes...")
        time.sleep(time_wait*60)