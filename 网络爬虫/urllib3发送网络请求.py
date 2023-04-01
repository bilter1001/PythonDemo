#导入模块
import urllib3


#创建PoolManager对象，用于处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
#对需要爬取的网页发送请求
response = http.request('GET','https://www.baidu.com/')
#打印读取的内容
print(response.data)

#获取网页中的图片信息
response = http.request('GET','https://www.baidu.com/img/bd_logo1.png')

#打印读取的内容 (图片信息)
print(response.data)