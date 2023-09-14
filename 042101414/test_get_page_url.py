from maincode import get_page_url
import pandas as pd

page_url = get_page_url(10)

df = pd.DataFrame()
df["弹幕"] = page_url
# df.to_excel("test_get_page_url.xlsx")
# print(page_url)
