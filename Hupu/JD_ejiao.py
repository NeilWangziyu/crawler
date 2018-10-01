import requests
from urllib.parse import urlencode
import lxml
from lxml import html
from lxml import etree
import re
import xlwt

itempage = 'https://item.jd.com/1397042360.html#comment'


workbook = xlwt.Workbook()
sheet = workbook.add_sheet("sheet1")
style = xlwt.easyxf('font: bold 1')
sheet.write(0, 0, itempage, style)
sheet.write(0, 1, 'Title', style)

count = 2


base_URL = 'https://sclub.jd.com/comment/productPageComments.action?'



for i in range (100):
    params = {
        'callback':'fetchJSON_comment98vv4195',
        'productId':'1397042360',
        'score':'0',
        'sortType':'5',
        'page':'{}'.format(i),
        'pageSize':'10',
        'isShadowSku':'0',
        'rid':'0',
        'fold':'1'
    }

    URL = base_URL + urlencode(params)
    try:
        detailhtml = requests.get(URL, timeout=3).content
    except:
        print("fail to gain file, page:",i)
        break

    text = detailhtml.decode('GBK')

    re_text = '"content":"\W+"'

    result = re.findall(r'(\"content\"\:\")(\S+)(\"\,)', text)

    for each in result:
        sheet.write(count, 0, each)
        count = count + 1

    print("finished page",i)

print("finished")
workbook.save("JD.xls")


# URL = base_URL + urlencode(params)
# print(URL)
# detailhtml = requests.get(URL, timeout=3).content
# print(detailhtml.decode('GBK'))
#
