import requests
import lxml
from lxml import html
import xlwt


workbook = xlwt.Workbook()
sheet = workbook.add_sheet("sheet1")
style = xlwt.easyxf('font: bold 1')
sheet.write(0, 0, 'Title', style)
sheet.write(0, 1, 'Ref', style)
sheet.write(0, 2, 'Author', style)
sheet.write(0, 3, 'Time', style)
sheet.write(0, 4, 'Auther_href', style)
sheet.write(0, 5, '性别', style)
sheet.write(0, 6, '所在地', style)
sheet.write(0, 7, '关注人', style)
sheet.write(0, 8, '访问者', style)


count = 0
for page in range(1, 10):
    baseURl = 'https://bbs.hupu.com/bxj-{}'.format(page)
    detailhtml = requests.get(baseURl, timeout=3)
    detailpc = detailhtml.text
    detailpc.encode('utf-8')
    detail_page = lxml.html.fromstring(detailpc)

    li = detail_page.xpath('//ul[@class="for-list"]/li')

    for each_li in li:
        count = count + 1

        #     # get names
        title_tem = each_li.xpath(".//a[@class='truetit']/text()")
        if len(title_tem) == 0:
            title = each_li.xpath(".//a[@class='truetit']/b/text()")
        else:
            title = title_tem
        sheet.write(count, 0, title[0])



        ref_get = each_li.xpath(".//a[@class='truetit']/@href")

        wholeref = 'https://bbs.hupu.com/' + ref_get[0]
        sheet.write(count, 1, wholeref)


        author_get = each_li.xpath(".//a[@class='aulink']/text()")
        if len(author_get) == 0:
            author = '无'
        else:
            author = author_get[0]
        sheet.write(count, 2, author)


        time_get = each_li.xpath(".//a[@style='color:#808080;cursor: initial; ']/text()")
        if len(time_get) == 0:
            time = '无'
        else:
            time = time_get[0]
        sheet.write(count, 3, time)


        author_href_get = each_li.xpath(".//a[@class='aulink']/@href")
        if len(author_href_get) == 0:
            author_href = '无'
        else:
            author_href = author_href_get[0]
        sheet.write(count, 4, author_href)

        #对发帖人的信息搜索
        authorhtml = requests.get(author_href, timeout=3)
        autherpc = authorhtml.text
        autherpc.encode('utf-8')
        auther_page = lxml.html.fromstring(autherpc)

        gender_get = auther_page.xpath(".//span [@itemprop='gender']/text()")
        if len(gender_get)==0:
            gender = ''
        else:
            gender = gender_get[0]
        sheet.write(count, 5, gender)

        address_get = auther_page.xpath(".//span [@itemprop='address']/text()")
        if len(address_get)==0:
            address = ''
        else:
            address = address_get[0]
        sheet.write(count, 6, address)

        # 关注的人:
        all_people_follow = []
        people_list = auther_page.xpath('.//div[@id="following"]/ul')
        for each in people_list:
            title_tem = each.xpath(".//a[@class='u']/@href")
            if len(title_tem):
                for length in range(len(title_tem)):
                    all_people_follow.append(title_tem[length])
            else:
                pass

        all_people = ' '.join(all_people_follow)
        sheet.write(count, 7, all_people)

        #访问者：
        all_people_visit = []
        people_list = auther_page.xpath('.//div[@id="visitor"]/ul')
        for each in people_list:
            title_tem = each.xpath(".//a[@class='u']/@href")
            if len(title_tem):
                for length in range(len(title_tem)):
                    all_people_visit.append(title_tem[length])
            else:
                pass
        all_people = ' '.join(all_people_visit)
        sheet.write(count, 8, all_people)

        #对帖子内容的检索


    print('finish page ', page)

workbook.save("test.xls")

