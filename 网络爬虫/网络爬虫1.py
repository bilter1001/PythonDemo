from cgitb import html
import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError

def download(url, user_agent='wswp', num_retries=2):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        html = urllib.request.urlopen(request).read()
    except (URLError,HTTPError,ContentTooShortError) as e:
        print("Download Error:", e.reason)
        html=None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, user_agent, num_retries -1)
    return html

#download('http://httpstat.us/500')
download('http://meetup.com')
