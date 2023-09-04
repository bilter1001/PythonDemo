import requests
from bs4 import BeautifulSoup

url = 'https://nd99u.site.101.com/onlineexam_web/index.html?online_exam_id=956aeb95-b6c0-4a6a-8f84-563e2af21b0a&sdp-app-id=b4fb92a0-af7f-49c2-b270-8f62afac1133&sdp-org-id=&sdp-biz-type=#/analysis/91bfca3b-64d4-4db0-bce6-2f6ab2a70b67'

def get_page_content(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  return soup

page_content = '' 

soup = get_page_content(url)
page_content += soup.find('body').text

# 获取分页内容
next_page = soup.find('a', {'class': 'next-page'})
while next_page:
  url = next_page['href']
  soup = get_page_content(url) 
  page_content += soup.find('body').text

  soup = BeautifulSoup(page_content, 'html.parser')
  next_page = soup.find('a', {'class': 'next-page'})

print(page_content)