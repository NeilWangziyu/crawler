from bs4 import BeautifulSoup
import requests
import re
import os
import lxml
from lxml import html
import os

URLs = []
for i in range(1,20):
    tem_url = "http://www.ivsky.com/tupian/chengshilvyou/" + "index_"+ str(i)+ ".html"
    print(tem_url)
    URLs.append(tem_url)

for URL in URLs:
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'lxml')
    img_uls = soup.find_all('div', {"class": "il_img"})
    for img_ul in img_uls:
        # print(img_ul)
        suburls = img_ul.find_all('a')[0]
        # print(suburls)
        url = suburls.find_all(re.compile('["/tupian/]'))
        print(url)
        # href = suburls[0].find_all(attrs={'target':'_blank'})
        # print(href)
        # for suburl in suburls:
        #     url = suburls.get('href')
        #     print(url)




# html = requests.get(URL).text
# soup = BeautifulSoup(html, 'lxml')
# img_uls = soup.find_all('div', {"class":"il_img"})
# for img_ul in img_uls:
#     # print(img_ul)
#     imgs = img_ul.find_all("a")
#     for img in imgs:
#         print(img)
#
# detailhtml = requests.get(URL)
# detailpc = detailhtml.text
# detailpc.encode('utf-8')
# detail_page = lxml.html.fromstring(detailpc)
# xpath = detail_page.xpath('/html/body/div[3]/div[3]/div[4]/div[2]/p/text()')
# print(xpath)
#
# #
# URL = "http://www.ivsky.com/tupian/"
# html = requests.get(URL).text
# soup = BeautifulSoup(html, 'lxml')
# img_ul = soup.find_all('div', {"class": "il_img"})
# # print(img_ul)
#
# os.makedirs('./img/', exist_ok=True)
#
# for ul in img_ul:
#     print(ul)
#     imgs = ul.find_all('img')
#     for img in imgs:
#         print(img)
#         url = img['src']
#         print(url)
#         r = requests.get(url, stream=True)
#         image_name = url.split('/')[-1]
#         with open('./img/%s' % image_name, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=128):
#                 f.write(chunk)
#             print('Saved %s' % image_name)
#
#
#
