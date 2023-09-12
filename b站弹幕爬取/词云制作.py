import jieba    #结巴分词
import wordcloud    #词云图
import imageio  #读取本地图片 修改词云图形

img = imageio.imread("D:\study\大三上课程资料\软件工程\B站弹幕大作业\OIP-C.jpg")
#1、读取弹幕数据
with open('弹幕6.txt',encoding='utf-8') as f:
    text = f.read()
    #jieba 结巴分词
    #2、分词，把一句话 分割成很多词汇
    text_list = jieba.lcut(text)
    #print(text_list)
    #列表转成字符串
    text_str = ' '.join(text_list)
    #3、词云图配置
    wc = wordcloud.WordCloud(
        width=500,#宽度
        height=500,#高度
        mask=img,
        stopwords={},
        background_color='white',#背景颜色
        font_path='msyh.ttc'#字体文件
    )
    wc.generate(text_str)
    wc.to_file('词云4.png')
    