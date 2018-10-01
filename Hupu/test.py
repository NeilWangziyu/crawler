import requests
from urllib.parse import urlencode
import lxml
from lxml import html
from lxml import etree
import re
import xlwt
import json

base_URL = 'https://sclub.jd.com/comment/productPageComments.action?'

params = {
        'callback':'fetchJSON_comment98vv222',
        'productId':'1411131635',
        'score':'0',
        'sortType':'5',
        'page':'1',
        'pageSize':'10',
        'isShadowSku':'0',
        'rid':'0',
        'fold':'1'
    }

URL = base_URL + urlencode(params)

detailhtml = requests.get(URL, timeout=3).content

text = detailhtml.decode('GBK')

result = re.findall(r'(\"content\"\:\")(\S+)(\"\,)', text)

print(result)