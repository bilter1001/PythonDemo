import requests
from bs4 import BeautifulSoup

# 获取指定网页的HTML源代码
url = 'https://nd99u.site.101.com/onlineexam/ndu/online_exam/122fb9be-e6b1-4731-b379-803c48d90ef2/analysis?online_exam_id=ffd533b8-e9a5-40d7-8638-460c22005100&sdp-app-id=b4fb92a0-af7f-49c2-b270-8f62afac1133&lang=zh-CN'
response = requests.get(url)
html = response.text

# 解析HTML源代码，获取所有链接
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

# 循环访问每个链接，获取内容，并将结果存储到同一个md文件中
with open('results.md', 'w', encoding='utf-8') as f:
    for link in links:
        href = link.get('href')
        if href.startswith('http'):
            response = requests.get(href)
            content = response.text
            # 进一步处理内容，例如提取标题等
            f.write('# ' + title + '\n\n')
            f.write(content + '\n\n')