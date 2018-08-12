# -*- coding:utf-8 -*-
import requests
import re
import xlwt
import lxml
import os
import threading
from lxml import html

global counter
global IPpool
IPpool = []
class IP_pool():
    def __init__(self,url):
        rawIPlist = []
        html = requests.get(url)
        pc = html.text
        pc.encode('utf-8')
        page = lxml.html.fromstring(pc)
        IP = re.findall("\d+.\d+.\d+.\d+:\d+", page.text)
        for line in IP:
            rawIPlist.append(line)
        for each in rawIPlist:
            IP = re.findall("\d+.\d+.\d+.\d+", each)
            if len(IP) != 0:
                print("testing", IP[0])
                return1 = os.system('ping -n 2 -w 1 %s' % IP[0])
                if return1:
                    print('IP %s is dead' % IP[0])  # 失败
                else:
                    print('IP %s is alive' % IP[0])  # 成功
                    IPpool.append(each)
        print(IPpool)

    def get_new_ip(self,url):
        rawIPlist = []
        html = requests.get(url)
        pc = html.text
        pc.encode('utf-8')
        page = lxml.html.fromstring(pc)
        IP = re.findall("\d+.\d+.\d+.\d+:\d+", page.text)
        for line in IP:
            rawIPlist.append(line)
        for each in rawIPlist:
            IP = re.findall("\d+.\d+.\d+.\d+", each)
            if len(IP) != 0:
                print("testing", IP[0])
                return1 = os.system('ping -n 2 -w 1 %s' % IP[0])
                if return1:
                    print('IP %s is dead' % IP[0])  # 失败
                else:
                    print('IP %s is alive' % IP[0])  # 成功
                    IPpool.append(each)
            print(IP_pool)

    def fetch_ip(self):
        if len(IPpool) != 0:
            temp = "http://" + str(IPpool[0])
            del IPpool[0]
            return temp
        else:
            self.get_new_ip(url)
            temp = "http://" + str(IPpool[0])
            del IPpool[0]
            return temp


def get_content(rawID,sheet,counter,proxies):
    ID1 = rawID[:12]
    ID2 = rawID[12]
    url = "http://so.baiten.cn/detail/patentdetail/63/CN" + ID1 + "." + ID2 + "/25"
    print("processing:" + url)
    print(proxies)
    sheet.write(counter, 9, url)
    detailhtml = requests.get(url,proxies=proxies, timeout = 3)
    detailpc = detailhtml.text
    detailpc.encode('utf-8')
    detail_page = lxml.html.fromstring(detailpc)

    title = detail_page.xpath('//*[@id="patTitle"]/text()')
    print("专利名:" + title[0])
    sheet.write(counter, 0, title[0])

    request_num = detail_page.xpath('//*[@id="pd-d-detail"]/div[1]/div/table/tr[1]/td[1]/span/text()')
    print("申请号:" + request_num[0])
    sheet.write(counter, 1, request_num[0])

    request_date = detail_page.xpath('//*[@id="pd-d-detail"]/div[1]/div/table/tr[2]/td[1]/a/text()')
    print("申请日:" + request_date[0])
    sheet.write(counter, 2, request_date[0])

    public_num = detail_page.xpath('//*[@id="pd-d-detail"]/div[1]/div/table/tr[2]/td[2]/a/text()')
    print("公开号:" + public_num[0])
    sheet.write(counter, 3, public_num[0])

    public_date = detail_page.xpath('//*[@id="pd-d-detail"]/div[1]/div/table/tr[3]/td[1]/a/text()')
    print("公开日:" + public_date[0])
    sheet.write(counter, 4, public_date[0])

    main_category_num = detail_page.xpath('//*[@id="pd-d-detail"]/div[1]/div/table/tr[4]/td[2]/a/text()')
    print("主分类号:" + main_category_num[0])
    sheet.write(counter, 5, main_category_num[0])

    author = detail_page.xpath('//*[@id="pd-d-detail"]/div[1]/div/table/tr[3]/td[2]/a/text()')
    authorstr = author[0]
    for i in range(1, len(author)):
        authorstr = authorstr + '、' + author[i]
    print("申请/专利权人：" + authorstr)
    sheet.write(counter, 6, authorstr)

    innovator = detail_page.xpath('//*[@id="pd-d-detail"]/div[1]/div/table/tr[4]/td[1]/a/text()')
    innovatorstr = innovator[0]
    for i in range(1, len(innovator)):
        innovatorstr = innovatorstr + '、' + innovator[i]
    print("发明/设计人：" + innovatorstr)
    sheet.write(counter, 7, innovatorstr)

    abstract = detail_page.xpath('///*[@id="pd-d-detail"]/div[2]/div[1]/p/text()')
    print("摘要:" + abstract[0])
    sheet.write(counter, 8, abstract[0])


if __name__ == "__main__":
    url = 'http://td.tudoudaili.com/ip/?tid=555201805942010&num=10&delay=3&sortby=time&foreign=none'
    ipp = IP_pool(url)
    proxies = {}
    f = open('patentID.txt','r')
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("sheet1")
    style = xlwt.easyxf('font: bold 1')
    sheet.write(0, 0, '专利名', style)
    sheet.write(0, 1, '申请号', style)
    sheet.write(0, 2, '申请日', style)
    sheet.write(0, 3, '公开号', style)
    sheet.write(0, 4, '公开日', style)
    sheet.write(0, 5, '主分类号', style)
    sheet.write(0, 6, '申请/专利权人', style)
    sheet.write(0, 7, '发明/设计人', style)
    sheet.write(0, 8, '摘要', style)
    sheet.write(0, 9, '详细信息', style)
    counter = 1
    patentID = f.readlines()
    while(len(patentID) != 0):
        aliveip = ipp.fetch_ip()
        proxies['https'] = aliveip
        rawID = patentID[0]
        while(True):
            try:
                rawID = patentID[0]
                get_content(rawID,sheet,counter,proxies)
                counter = counter + 1
                del patentID[0]
            except:
                break

    f.close()
    workbook.save("patents.xls")


