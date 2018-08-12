from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests



# if has Chinese, apply decode()
html = urlopen("https://blog.csdn.net/CY_TEC/article/details/48996355").read().decode('utf-8')
# print(html)

# res = re.findall('<title>([\s \S]*)</title>', html)
# print('\n Page title is:', res)
#
# res = re.findall('<script type="application/ld+json">([\s \S]*)</script>', html)
# print('\n Page  is:', res)

soup = BeautifulSoup(html, features='lxml')
print(soup.head)
print('--------------------')
print(soup.h1)
print('--------------------')
print(soup.span)
print('--------------------')
print('\n', soup.p)
print('--------------------')


all_href = soup.find_all('href')
# all_href = [l['link href'] for l in all_href]
print('\n', all_href)

