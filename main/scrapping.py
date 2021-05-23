import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
response = requests.get(url)
response.text
# response.json()

# %%

html = requests.get("https://finance.naver.com/item/main.nhn?code=000660").text
soup = BeautifulSoup(html, "html5lib")

# CSS selector
tags = soup.select("#_per")
tags = soup.select("table tbody tr td em")
tags = soup.select(".lwidth tbody .strong td em")# tbody with style .lwidth. then td with style .string.
tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")
tags = soup.select("#tab_con1 > div:nth-of-type(2) > table > tbody > tr.strong > td > em")
tag = tags[0]
print(tag.text)
