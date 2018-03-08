import itchat
from pyecharts import Pie, Bar
from pandas import DataFrame
import re
import jieba
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

# 先登录
itchat.login()
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0
for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])
print('male:{}\nfemale:{}\nother:{}\n'.format(male, female, other))

# 性别饼图
attr = ['男性好友', '女性好友', '不明好友']
v1 = [84, 64, 11]
pie = Pie('性别比例')
pie.add('', attr, v1, is_label_show=True)
pie.render('render1.html')


# 存储好友信息
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


Nickname = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signa = get_var('Signature')
date = {'Nickname': Nickname,
        'Sex': Sex,
        'Province': Province,
        'City': City,
        'Signa': Signa,
        }
frame = DataFrame(date)
frame.to_csv('date2.csv', index=True)

# 省份分布图
Provinces = []
for p in friends:
    Province = p.Province
    Provinces.append(p.Province)

a = {}
for i in Provinces:
    a[i] = Provinces.count(i)

b = sorted(a.items(), key=lambda item: item[1])

attrs = []

values = []

j = 0
while j < len(b):
    attr = b[j][0]
    value = b[j][1]
    attrs.append(attr)
    values.append(value)
    j += 1

bar = Bar('')
bar.add('好友省份分布', attrs, values, is_datazoom_show=True)
bar.render()

# 个性签名图云
siglist = []
for i in friends:
    sig = i['Signature'].strip().replace('span', '').replace('emoji', '')
    rep = re.compile('1f\d+\w%|[<>/=]')
    sig = rep.sub('', sig)
    siglist.append(sig)
text = ''.join(siglist)

wordlist = jieba.cut(text, cut_all=True)
word_space_spilt = ' '.join(wordlist)

color = np.array(Image.open("1.png"))
my_wc = WordCloud(background_color='white',
                  max_words=700,
                  mask=color,
                  max_font_size=60,
                  random_state=40,
                  scale=2,
                  font_path="/home/lanroot/桌面/wechat/msyh.ttc",
                  ).generate(word_space_spilt)
img_color = ImageColorGenerator(color)
plt.imshow(my_wc.recolor(color_func=img_color))
plt.imshow(my_wc)
plt.axis('off')
plt.show()
