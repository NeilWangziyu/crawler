import requests
from lxml import etree

# url = 'https://movie.douban.com/subject/1292052/'
# data = requests.get(url).text
# s=etree.HTML(data)
#
# film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
# director=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
# actor=s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
# time=s.xpath('//*[@id="info"]/span[13]/text()')
#
# print('电影名称：',film)
# print('导演：',director)
# print('主演：',actor)
# print('片长：',time)


from lxml import etree
import requests
import time

for a in range(1, 6):
    url = 'http://cd.xiaozhu.com/search-duanzufang-p{}-0/'.format(a)
    data = requests.get(url).text

    s = etree.HTML(data)
    file = s.xpath('//*[@id="page_list"]/ul/li')
    time.sleep(3)

    for div in file:
        title = div.xpath("./div[2]/div/a/span/text()")[0]
        price = div.xpath("./div[2]/span[1]/i/text()")[0]
        scrible = div.xpath("./div[2]/div/em/text()")[0].strip()
        pic = div.xpath("./a/img/@lazy_src")[0]

        print("{}   {}   {}   {}\n".format(title, price, scrible, pic))