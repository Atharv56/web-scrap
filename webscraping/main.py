from bs4 import BeautifulSoup
with open('D:\Code\Github codes\web-scrap\webscraping\home.html', 'r') as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    print("Here is the price list for different courses: ")
    print("There you go")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'{course_name} costs {course_price}')

    