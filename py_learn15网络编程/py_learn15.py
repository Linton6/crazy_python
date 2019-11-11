# 第15章
'''
from urllib.parse import *
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)
print('scheme:',result.scheme, result[0])
print('主机和端口：',result.netloc, result[1])
print("主机：", result.params)
print("端口：",result.geturl)

from urllib.request import *
result = urlopen('http://about.uuspider.com/2015/07/20/decode.html')
data = result.read()
print(data.decode('utf-8'))
'''

# 1.编写一个程序，使用urllib.request读取http://www.crazyit.org首页的内容
# '''
# from urllib.request import *
# result = urlopen('http://www.crazyit.org/forum.php')
# data = result.read()
# print()
# f = open(r'G:\08 Code\Python\crazy_python\py_learn15网络编程\url.txt','w+')
# f.write(data.decode('utf-8'))
# f.close
# '''

# 2.编写一个程序，结合使用urllib.request和re模块，下载并识别http://www.crazyit.org首页的全部链接地址
# '''
# from urllib.request import *
# import re , os, fileinput
# result = urlopen('http://www.crazyit.org/forum.php')
# data = result.read()
# print()
# f = open(r'G:\08 Code\Python\crazy_python\py_learn15网络编程\url.txt','w+')
# r = open(r'G:\08 Code\Python\crazy_python\py_learn15网络编程\result_url.txt','w+')
# f.write(data.decode('utf-8'))
# url_pat = re.compile(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?')
# for line in fileinput.input(files=(r'G:\08 Code\Python\crazy_python\py_learn15网络编程\url.txt',)):
#     m = re.findall(url_pat, line)
#     # print(type(m))
#     for e in range(len(m)):
#         s = "".join(m[e])  # 这边出的问题是列表里的元素是元组，所以不能直接用write函数
#         print(s)
#         r.write(s + os.linesep)
# fileinput.close()
# r.close()
# f.close()
# '''



# 3.开发并完善本章介绍的聊天室程序，并为该程序提供界面。

# 4.开发并完善本章介绍的多点广播程序，并为该程序提供界面，使之成为一个局域网内的聊天程序。

# 5.结合使用smptlib和poplib模块，开发一个简单的邮件客户端程序，该客户端程序既可以发送邮件，也可以接受邮件