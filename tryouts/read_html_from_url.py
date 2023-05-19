'''
Сколько HTML-тегов в коде главной страницы сайта jetlend.ru?
Сколько из них содержит атрибуты?

Напишите скрипт на Python, который выводит ответы на вопросы выше.
'''

from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://jetlend.ru/tests/test-senior-backend-python'

driver = webdriver.Chrome()
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')
texts = soup.find_all('textarea')
for text in texts:
    print(text)
driver.quit()

print(f'Count of HTML tags: {len(soup.find_all())}')




