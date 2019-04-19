import requests
from urllib.parse import urlencode
import lxml
from lxml import html
from lxml import etree
import re
import xlwt
import time
from bs4 import BeautifulSoup

link_pool = []
linked_hash = set()
base_url = r'https://www.cisco.com'
count = 1
link_pool.append("https://www.cisco.com/c/en/us/products/routers/product-listing.html")
for each in link_pool:

    if count > 5:
        break
    if each not in linked_hash:
        if len(linked_hash) != 0:
            link = base_url + each
        else:
            link = each
        linked_hash.add(link)
        print(link)
        try:
            detailhtml = requests.get(link, timeout=3).content
            text = detailhtml.decode('utf-8')
            webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
            lined_found = webpage_regex.findall(text)
            link_pool += lined_found

            soup = BeautifulSoup(detailhtml)

            title_file = soup.title.contents[0]
            saved_File = r'\\result' + r'\\' + title_file + '.txt'

            fo = open(saved_File, 'w')

            webpage_regex = re.compile('<p class="pBody">.*</p>', re.IGNORECASE)
            content_raw = webpage_regex.findall(text)
            for each in content_raw:
                each = re.sub(r"<.*?>", "", each)

            fo.writelines(each)



            webpage_regex = re.compile(r'<td>.*</td>')
            table_raw = webpage_regex.findall(text)
            for each in table_raw:
                each = re.sub(r"<.*?>", "", each)

            fo.writelines(each)



            fo.close()

            time.sleep(5)
            count += 1
            print(count, "finish ", saved_File)


        except Exception as e:
            print(e)
            time.sleep(5)
            continue





