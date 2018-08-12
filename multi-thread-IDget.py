# -*- coding:utf-8 -*-
import requests
import re
import xlwt
import lxml
from lxml import html
import threading
from time import ctime,sleep
from queue import Queue
import random
import time
from lxml import etree

lock = threading.Lock()
global i
#注意这里有一个bug，page只能是1或者大于5的数字....，当专利数量大于20小于100时有错误
def f_getpagenum(data,category):
    data["pageNow"] = 1
    data["strSources"] = category
    t = 0
    print(time.ctime())
    html_post = requests.post(url,data=data)
    selector_post = etree.HTML(html_post.text)
    pagenum = selector_post.xpath("/html/body/div[3]/div[2]/div/a[7]/text()")
    if len(pagenum) >= 1:
        return int(pagenum[0])
    else:
        return 1

def run_f_getid(data,category,i ,f):
    lock.acquire()
    try:
        f_getid(data,category,i,f)
    finally:
        lock.release()


def f_getid(data,category,i,f):
    data["strSources"] = category
    print("page:",i)
    data["pageNow"] = i
    html_read = requests.post(url, data=data)
    selector_read = etree.HTML(html_read.text)
    content = selector_read.xpath("/html/body/div[3]/div[2]/table/tr/td/table/tr/td[2]/a/text()")
    for each in content:
        patentID = re.search("(\w{13})|(\w{9})", each).group(0)
        print(patentID)
        f.writelines(patentID+ '\n')
    print("page:%s,time:%s"%(i,time.ctime()))

def run_f_getid(data, category, i, f):
    lock.acquire()
    try:
        f_getid(data, category, i, f)
    finally:
        lock.release()


#这里只提取关键词为20160914的专利ID
if __name__ == "__main__":
    year = "2016"
    month = "09"
    day = "14"
    i = 0
    f = open('content.txt', 'w')
    url='http://epub.sipo.gov.cn/patentoutline.action'
    data = {
        "showType": "0",
        "strSources": "",
        "strWhere": "",
        "numSortMethod": "4",
        "strLicenseCode": "",
        "numIp": "",
        "numIpc": "",
        "numIg": "",
        "numIgc": "",
        "numIgd": "",
        "numUg": "",
        "numUgc": "",
        "numUgd": "",
        "numDg": "",
        "numDgc": "",
        "pageSize": "20",
        "pageNow": "1",
    }
    #非发明解密
    # pip:发明公布
    # pipc:发明公布更改
    # pig:发明授权
    # pigc:发明授权更改
    # pug:实用新型
    # pugc:实用新型更改
    data["strWhere"] = "AD, OPD, CPD, DPD, PD, ENPD += '"+year+"."+month+"."+day+"'"
    for category in ["pip","pug"]:
        #only pip and pug
        print("专利类型："+ category)
        data["strSources"] = category
        data["pageNow"] = 1
        pagenum = f_getpagenum(data,category)
        print("总共页数：",pagenum)
        data["pageNow"] = 1
        data["strSources"] = category
        if pagenum != 1:
            i = 1
            while(i <= 20 + 1): #5个线程
                for temp in range(1,5):
                    name = str(temp)
                    name = threading.Thread(target=run_f_getid, args=(data,category, i, f))
                    name.start()
                    i = i + 1
                    name.join()
        else:
            html_read = requests.post(url, data=data)
            selector_read = etree.HTML(html_read.text)
            content = selector_read.xpath("/html/body/div[3]/div[2]/table/tr/td/table/tr/td[2]/a/text()")
            if len(content) != 0:
                for each in content:
                    patentID = re.search("(\w{13})|(\w{9})", each).group(0)
                    print(patentID)
                    f.writelines(patentID + '\n')
                print("page:1,time:%s" % (time.ctime()))
            else:
                print("类型：" + category + "——无数据")

    #发明解密
    # for category in ["pugd"]:
    #     print("专利类型："+ category)
    #     data["strSources"] = category
    #     data["pageNow"] = 1
    #     pagenum = f_getpagenum(data,category)
    #     print("总共页数：",pagenum)
    #     data["strSources"] = category
    #     html_read = requests.post(url, data=data)
    #     selector_read = etree.HTML(html_read.text)
    #     content = selector_read.xpath("/html/body/div[3]/div[2]/table/tr/td/table/tr/td[2]/a/text()")
    #     if len(content) != 0:
    #         for each in content:
    #             patentID = re.search("(\w{13})|(\w{9})", each).group(0)
    #             print(patentID)
    #             f.writelines(patentID + '\n')
    #         print("page:1,time:%s" % (time.ctime()))
    #     else:
    #         print("类型：" + category + "——无数据")

    f.close()


