from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("http://tieba.baidu.com/f?kw=%E6%8A%80%E6%9C%AF%E5%AE%85&red_tag=l0192983224").read().decode('utf-8')
# print(html)

soup = BeautifulSoup(html, features='lxml')


print(soup.head.get_text())

month = soup.find_all('div', {"class": "top_cont_title"})
for m in month:
    print(m.get_text())

# #
# #
# # jan = soup.find('u1', {'class':'jan'})
# # d_jan = jan.find_all('li')
# # for d in d_jan:
# #     print(d.get_text())

# html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
