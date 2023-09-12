from maincode import get_page_url,get_inter_urls
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().chrome
}
cookies = "buvid3=CB06A7AA-06EA-E219-1FF8 -C17A8AEF2B5F51873infoc; i-wanna-go-back=-1; _uuid=F101D6524-C221-A9C10-97DA-542B815FEDCA51202infoc; FEED_LIVE_VERSION=V8; DedeUserID=522530792; DedeUserID__ckMd5=2e03492b99caef5f; header_theme_version=CLOSE; rpdid=|(mmJlJm|JR0J'uY)mmRlRJm; CURRENT_BLACKGAP=0; b_nut=1689995419; buvid_fp_plain=undefined; LIVE_BUVID=AUTO8416913939503688; b_ut=5; CURRENT_FNVAL=4048; CURRENT_QUALITY=120; fingerprint=1aca2908ee5dcb47b78992b83443d802; buvid4=62276AB2-9F0B-5D92-6F2F-CC9D23C9BF5952837-023072121-82E7TcOSVfD+L2qAouj/fw%3D%3D; buvid_fp=1aca2908ee5dcb47b78992b83443d802; SESSDATA=2d977c9e%2C1709471583%2C72995%2A926-DRT6OVPk1scEko_98M-DBiJGNXq-FpwsmqeV7GXGAD5uZU1YqSGc2gnRJ0fI0pQZ6hdAAAXAA; bili_jct=d77d112e4a880ed95e701a2cf3036e74; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQxNzg3ODgsImlhdCI6MTY5MzkxOTU4OCwicGx0IjotMX0.tzYoMaEgtMiZTcF9uQOUuTyLNAQk9C9V8b6RoB0_ck0; bili_ticket_expires=1694178788; home_feed_column=5; bp_video_offset_522530792=838082259895451672; b_lsid=5DEC104C10_18A68FFEEF4; bsource=search_bing; browser_resolution=1699-944; sid=8ilhuxa6; PVID=12"
dic_cookies = {}
for i in cookies.split("; "):
    dic_cookies[i.split("=")[0]] = i.split("=")[1]

page_url_list = get_page_url(10)
first_page_url = page_url_list[0]
first_page_all_vedio_url = get_inter_urls(url=first_page_url,headers=headers,cookies=dic_cookies)
# print(first_page_all_vedio_url)