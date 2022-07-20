from cgitb import html
import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError
import itertools


def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(charset)
    except (URLError,HTTPError,ContentTooShortError) as e:
        print("Download Error:", e.reason)
        html=None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, user_agent, num_retries -1)
    return html


def crawl_sitemap(url, max_errors = 5):
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url,page)
        html = download(pg_url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                # 达到最大错误次数，退出循环
                break
            else:
                num_errors = 0
                # 成功，可以爬取到结果



crawl_sitemap('http://example.python-scraping.com/view/-')



