import requests
import lxml
from lxml import html

URL = 'https://my.hupu.com/258051531319630'
URL_2 = 'https://my.hupu.com/68154067684448'
URL_3 = 'https://my.hupu.com/53347953706220'
URL_4 = 'https://my.hupu.com/185941226680433'
URL_5 = 'https://my.hupu.com/19415579077176'
URL_6 = 'https://my.hupu.com/dennisdo'

detailhtml = requests.get(URL_2, timeout=3)
detailpc = detailhtml.text
detailpc.encode('utf-8')
detail_page = lxml.html.fromstring(detailpc)

# 性别，所在地，加入时间，NBA主队
person = detail_page.xpath(".//span [@class='f666']/text()")
print(len(person))
print(person)
# NBAsupport = detail_page.xpath("//*[@id='main']/div[1]/div[2]/div/span[6]/a/text()")
# print(NBAsupport)

gender = detail_page.xpath(".//span [@itemprop='gender']/text()")
print(gender)

address = detail_page.xpath(".//span [@itemprop='address']/text()")
print(address)

people_list = detail_page.xpath('.//div[@id="following"]/ul')
for each in people_list:
    title_tem = each.xpath(".//a[@class='u']/@href")
    print(title_tem)

people_list = detail_page.xpath('.//div[@id="visitor"]/ul')
print(people_list)
for each in people_list:
    title_tem = each.xpath(".//a[@class='u']/@href")
    print(title_tem)