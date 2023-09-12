import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import time
import os


def get_page_url(n):
    '''
    分页网址url的采集
    n:爬取页数
    return:得到分页网页的list
    '''
    url_list = []
    for i in range(n):
        url = f'https://search.bilibili.com/all?vt=80749902&keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%B0%B4%E6%8E%92%E6%B5%B7&page={i+1}'
        url_list.append(url)
    return url_list


def get_inter_urls(url, headers, cookies):
    '''
    视频页面url采集
    ui：视频信息页面url(页面中的)
    headers：请求头部信息
    cookies：cookies信息
    结果：得到一个视频页面所有视频的list
    '''
    ri = requests.get(url=url, headers=headers, cookies=cookies)
    soupi = BeautifulSoup(ri.text, 'lxml')
    lis = soupi.find('div', class_="video-list row")
    if lis is None:
        print("未找到视频列表")
        return []

    lis = lis.find_all('div')
    lst = []
    for li in lis:
        if li.a is not None:
            lst.append('https:' + li.a['href'])
    return lst


# url = "https://search.bilibili.com/all?vt=80749902&keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%B0%B4%E6%8E%92%E6%B5%B7"
# resp = requests.get(url,headers=headers,cookies=dic_cookies)

# print(get_inter_urls(url,headers=headers,cookies=dic_cookies))

def get_data(url, headers, cookies):
    '''
    先获取cid
    获取页面弹幕数据
    ui:视频页面网址（）
    headers:user-agent信息
    cookies:cookies信息
    '''
    # 获取前10页的网址
    # urllst = get_url(10)
    # 获取第一页的全部20个视频url
    # u1 = urllst[0]
    # 获取第一个视频的url
    # url_inter_1 = get_inter_urls(ui,headers=headers,cookies=dic_cookies)[0]
    ri = requests.get(url=url, headers=headers, cookies=cookies)
    # soupi = BeautifulSoup(ri.text,'lxml')
    # title = soupi.find(id = "viewbox_report").h1.text
    # print(title)
    cid = re.search(r'"cid":(\d*),', ri.text).group(1)
    # print(cid)
    cid_url = f"https://api.bilibili.com/x/v1/dm/list.so?oid={cid}"
    r2 = requests.get(cid_url)
    r2.encoding = r2.apparent_encoding
    data_list = []
    soup2 = BeautifulSoup(r2.text, "xml")
    d_elements = soup2.find_all("d")
    for d_element in d_elements:
        data_list.append(d_element.text)
    # print(data_list)
    # 将弹幕存储进txt文件
    with open("弹幕6.txt",mode="a",encoding="utf-8") as f:
        for data in data_list:
            f.write(data)
            f.write("\n")

    # 将弹幕存储进excel文件
    # df = pd.DataFrame(data_list, columns=['弹幕'])
    # if not os.path.exists("弹幕6.xlsx"):
    #     df.to_excel("弹幕6.xlsx", 'SelectData', index=False)
    # else:
    #     with pd.ExcelWriter("弹幕6.xlsx", engine='openpyxl', mode='a') as writer:
    #         df.to_excel(writer, 'SelectData', index=False)



if __name__ == "__main__":
    # #设置请求头headers和登录信息cookies
    start_time = time.time()
    headers = {
        'User-Agent': UserAgent().chrome
    }
    cookies = "buvid3=CB06A7AA-06EA-E219-1FF8 -C17A8AEF2B5F51873infoc; i-wanna-go-back=-1; _uuid=F101D6524-C221-A9C10-97DA-542B815FEDCA51202infoc; FEED_LIVE_VERSION=V8; DedeUserID=522530792; DedeUserID__ckMd5=2e03492b99caef5f; header_theme_version=CLOSE; rpdid=|(mmJlJm|JR0J'uY)mmRlRJm; CURRENT_BLACKGAP=0; b_nut=1689995419; buvid_fp_plain=undefined; LIVE_BUVID=AUTO8416913939503688; b_ut=5; CURRENT_FNVAL=4048; CURRENT_QUALITY=120; fingerprint=1aca2908ee5dcb47b78992b83443d802; buvid4=62276AB2-9F0B-5D92-6F2F-CC9D23C9BF5952837-023072121-82E7TcOSVfD+L2qAouj/fw%3D%3D; buvid_fp=1aca2908ee5dcb47b78992b83443d802; SESSDATA=2d977c9e%2C1709471583%2C72995%2A926-DRT6OVPk1scEko_98M-DBiJGNXq-FpwsmqeV7GXGAD5uZU1YqSGc2gnRJ0fI0pQZ6hdAAAXAA; bili_jct=d77d112e4a880ed95e701a2cf3036e74; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQxNzg3ODgsImlhdCI6MTY5MzkxOTU4OCwicGx0IjotMX0.tzYoMaEgtMiZTcF9uQOUuTyLNAQk9C9V8b6RoB0_ck0; bili_ticket_expires=1694178788; home_feed_column=5; bp_video_offset_522530792=838082259895451672; b_lsid=5DEC104C10_18A68FFEEF4; bsource=search_bing; browser_resolution=1699-944; sid=8ilhuxa6; PVID=12"
    dic_cookies = {}
    for i in cookies.split("; "):
        dic_cookies[i.split("=")[0]] = i.split("=")[1]

    # 获取前10页的网址
    urllst = get_page_url(10)
    # 获取第一页的视频url
    ul = urllst[0]
    # 获取第一页第一个视频url
    url_first = get_inter_urls(ul, headers=headers, cookies=dic_cookies)[0]
    # 获取cid，访问弹幕url，并保存到本地
    get_data(url=url_first, headers=headers, cookies=dic_cookies)
    end_time = time.time()
    print(end_time-start_time)
    # # url_pages = get_url(10)
    # # for page in url_pages:
    # #     lst = get_inter_urls(ui=page,headers=headers,cookies=dic_cookies)
    # #     for ls in lst:
    # #         get_data(ui=ls,headers=headers,cookies=dic_cookies)

    # #获取前10页的网址
    # urllst = get_page_url(10)
    # #获取第一页的全部20个视频url
    # u1 = urllst[0]
    # #获取第一个视频的url
    # url_inter_1 = get_inter_urls(u1,headers=headers,cookies=dic_cookies)[0]
    # ri = requests.get(url=url_inter_1,headers=headers,cookies=dic_cookies)
    # # soupi = BeautifulSoup(ri.text,'lxml')
    # # title = soupi.find(id = "viewbox_report").h1.text
    # # print(title)
    # cid = re.search(r'"cid":(\d*),',ri.text).group(1)
    # #print(cid)
    # cid_url = f"https://api.bilibili.com/x/v1/dm/list.so?oid={cid}"
    # r2 = requests.get(cid_url)
    # r2.encoding = r2.apparent_encoding
    # data_list = []
    # soup2 = BeautifulSoup(r2.text, "xml")
    # d_elements = soup2.find_all("d")
    # for d_element in d_elements:
    #     data_list.append(d_element.text)
    # # print(data_list)
    # with open("弹幕3.txt",mode="a",encoding="utf-8") as f:
    #     for data in data_list:
    #         f.write(data)
    #         f.write("\n")
