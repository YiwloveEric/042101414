'''
1、发送请求，对url发送请求
    需要注意点:
        -请求方式确定
        -请求头参数
2、获取数据，提取我们想要的数据内容，弹幕数据
3、保存数据，把获取下来的数据内容保存txt文本
https://api.bilibili.com/x/v1/dm/list.so?oid=1253321521
https://api.bilibili.com/x/v1/dm/list.so?oid=1245133831
https://api.bilibili.com/x/v1/dm/list.so?oid=1245383999
模拟浏览器对于服务器发送请求
'''

import requests
from fake_useragent import UserAgent
import re #正则表达式模块
#1、发送请求
url = "https://api.bilibili.com/x/v1/dm/list.so?oid=1258455335"
#headers请求头 将python代码进行伪装,模拟成浏览器去发送请求
headers = {
    'User-Agent':UserAgent().chrome
}
#2、获取数据
resp = requests.get(url=url,headers=headers)
resp.encoding = resp.apparent_encoding
print(resp.text)
#3、解析数据，解析方式，re[可以直接对于字符串数据进行提取] css xpath[主要根据标签属性/节点提取数据]
#()精确匹配 表示想要的数据 不加括号就是泛匹配 .*?正则表达式的元字符 表示通配符（除了\n)
data_list = re.findall(r'<d p=".*?">(.*?)</d>',resp.text)

for data in data_list:
    #mode 保存方式 encoding编码
    with open ('弹幕2.txt',mode='a',encoding='utf-8') as f:
        f.write(data)
        f.write('\n')
        

