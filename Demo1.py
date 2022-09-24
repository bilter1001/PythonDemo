# from distutils.log import debug
from cgi import print_arguments
from re import A
import sys

import urllib.request

# 字符串
str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print(sys.path.pop(1))

# list示例代码
lstWord = ['开心', 222, '谢谢', '没有', '东西', '123']
print(lstWord)

print(lstWord[:-1])
print(lstWord[::-1])  # 反转list


# list示例代码 反转list
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)
    return output


# 冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist


# 获取系统时间
def getTime():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 爬取网页的内容
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


# 遍历文件夹
def getFile(path):
    import os
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)
            print(os.path.join(root, file))


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    blist = bubbleSort(alist)
    print(blist)
    print(alist)
    print(alist[::-1])
    print(alist[-1::-1])
    print(alist[-2::-1])

    print(getTime())

    getFile('D:\我的文档\Pictures\作业指导书')
