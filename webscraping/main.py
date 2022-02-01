from bs4 import BeautifulSoup
with open('/Users/atharvsalian/Desktop/Github/web-scrap/web-scrap/webscraping/home.html', 'r') as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h5')
    print(tags)
    for tag in tags:
        print(tag.text) #to get all the content in 'h5' tag
