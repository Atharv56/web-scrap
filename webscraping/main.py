from bs4 import BeautifulSoup
with open('/Users/atharvsalian/Desktop/Github/web-scrap/web-scrap/webscraping/home.html', 'r') as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        