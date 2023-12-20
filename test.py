import requests
import re
from bs4 import BeautifulSoup

# ウェブページのURL（適宜URL設定する）
url = "https://www.trans-cosmos-digtec.co.jp/"

# ウェブページの取得
response = requests.get(url)

# レスポンスのテキストをBeautiful Soupで解析
soup = BeautifulSoup(response.text, "html.parser")

# テキストの抽出
text = soup.get_text()
text_without_spaces = re.sub(r'\s+', '', text)
print(text_without_spaces)