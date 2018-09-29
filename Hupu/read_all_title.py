import xlrd
import jieba
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


font = 'simsun.ttf'

data = xlrd.open_workbook('bxj_9_29.xls')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
print(nrows)
print(ncols)
text = table.col_values(0)
alltitles = []
for i in range(1, nrows):
    temp = text[i]
    temp = re.sub('\W', '', temp)

    seg_list = jieba.cut(temp, cut_all=False, HMM=True)
    # print(" ".join(seg_list))
    for each in seg_list:
        alltitles.append(each)
# print(alltitles)
text = " ".join(alltitles)
# print(text)

font = 'simsun.ttf'

stopwords = set(STOPWORDS)
stopwords.add('zt')

wc = WordCloud(background_color="white",collocations=False, font_path=font, width=1400, height=1400, margin=2,stopwords=stopwords).generate(text.lower())

plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file('虎扑步行街标题.png')
