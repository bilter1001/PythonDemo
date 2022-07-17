#导入模块
import urllib.request
#打开需要爬取的网页
response = urllib.request.urlopen('http://www.baidu.com')
#读取网页代码
html = response.read()
#打印读取的内容
print(html)