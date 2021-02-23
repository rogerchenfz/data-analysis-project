"""
    日期：2019.07.26.
    功能：词云图制作
"""

import jieba
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

comment = []
with open('jd_comment_26414687140.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        comment.append(row)

# 设置分词
comment_after_split = jieba.cut(str(comment), cut_all=False)
word = ''.join(comment_after_split)
print(word)

# 去掉不需要的词
stopwords = STOPWORDS.copy()
# 加入不需要的
stopwords.add('吃鸡神器')
stopwords.add('\n')
stopwords.add("n'")

# 导入背景图
bg_image = plt.imread('bg.jpg')    # 文件夹中
# 设置词云的参数
wc = WordCloud(width=1024, height=768, background_color='white', mask=bg_image,
               stopwords=stopwords, max_font_size=400)
# 分词后数据导入云图
wc.generate_from_text(word)

# 绘制图像
plt.imshow()
plt.axis('off')  # 不显示坐标轴
# 保存在本地
wc.to_file('词云图.jpg')

