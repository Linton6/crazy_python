#coding=utf-8
# 第12章
# 1.有两个磁盘文件text1.txt和text2.txt，各存放一行英文字母，要求把这两个文件中的信息合并（按照字母顺序排列），然后输出到一个新文件text3.txt中

'''import fileinput
import os
f = open(r'G:\08 Code\Python\crazy_python\py_learn12\text3.txt','w+')
for line in fileinput.input(files=(r'G:\08 Code\Python\crazy_python\py_learn12\text1.txt',r'G:\08 Code\Python\crazy_python\py_learn12\text2.txt')):
    print(fileinput.filename() , fileinput.filelineno() , line)
    print(type(line))
    f.write(line + os.linesep)
fileinput.close()
f.close()
'''

# 2.提示用户不断地输入多行内容，程序自动将内容保存到my.txt文件中，直到用户输入exit为止  
'''？？？？缺陷：没有把exit时退出功能实现'''

'''import sys
import os
f = open(r'G:\08 Code\Python\crazy_python\py_learn12\text3.txt','w+')
flg = True
while flg:
    line = sys.stdin.readline()
    if line in 'exit':
        flg = False
        print("结束1")
        # sys.exit()
        break 
    f.write(line)
    if not line:
        print("结束3")
        sys.exit()
        break
print("结束2")
f.close()'''

# for line in sys.stdin:
#     if line in 'exit':
#         print("结束1")
#         break
#     if not line:
#         print("结束2")
#         break
#     f.write(line)
# f.close()
# print("结束3")
    


# 3.实现一个程序，该程序提示用户输入一个文件路径，程序读取这个包含手机号的文本文件（该文件内容可能很大），
#要求程序能识别出该文件中所有的手机号码，并将这些手机号码保存到phone.txt文件中

'''
import fileinput
import sys
import os
import re
f = open(r'G:\08 Code\Python\crazy_python\py_learn12\phone.txt','w+')
phone_pat = re.compile(r'156\d{8}') #re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
for line in fileinput.input(files = (r'G:\08 Code\Python\crazy_python\py_learn12\text3.txt',r'G:\08 Code\Python\crazy_python\py_learn12\text1.txt')):
    # findall函数
    m = re.findall(phone_pat, line)
    for e in range(len(m)):
        f.write(m[e] +os.linesep)

    # finditer函数
fileinput.close()
f.close()
'''



# 4.实现一个程序，该程序提示用户输入一个目录，程序递归读取该目录及其子目录下所有能识别的文本文件，txt和py吧
# 要求程序能识别出所有文件中的所有手机号码，并将这些手机号码保存到phones.txt  
'''?????py文件老是报编码格式错误'''
'''
from pathlib import *
import re
import fileinput
import sys
import os
p = Path('.')
f = open(r'G:\08 Code\Python\crazy_python\py_learn12\phones.txt','w+', encoding='utf-8')
for x in p.glob('**/*'): # 获取该目录及其子目录下所有能识别的文本文件
    y = str(x)
    if (y == 'phones.txt') | (y == 'py_learn12.py'):
        continue
    if y.endswith('.txt') |y.endswith('.py')  :
        print(y)
        phone_pat = re.compile(r'[\d]{11}') #re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
        s = 'G:\\08 Code\\Python\\crazy_python\\py_learn12\\'
        s = s + y
        print("路径:",s)
        for line in fileinput.input(files = (s)):
            # findall函数
            m = re.findall(phone_pat, line)
            print("findall函数")
            print(len(m))
            for e in range(len(m)):
                f.write(m[e] +os.linesep)
        fileinput.close()

f.close()
'''

# 5.实现一个程序，该程序提示用户运行该程序时输入一个路径。该程序会将该路径下（及其子目录下）的所有文件列出来
"""
from pathlib import *
s = input("输入一个路径：")
p  = Path(s)
# print(type(p))
if type(p) == WindowsPath:
    print("输入的路径名有误")
for x in p.glob('**/*'):
    print(x)
    
"""
    



# 6.实现一个程序，当用户运行该程序时，提示用户输入一个路径。该程序会将该路径下的文件、文件夹的数量统计出来
from pathlib import *
import os

s = input("输入一个路径：")
p  = Path(s)
print(type(p))
# if type(p) in (WindowsPath,):
#     print("输入的路径名有误")
for x in p.iterdir():
    print(x)
print("========统计结果如下：========")
num1 = 0
num2 = 0
for root,dirs,files in os.walk(s, topdown=True):
    for name in files:
        num1 += 1
    for name in dirs:
        num2 += 1
print("文件数量：",num1)
print("子目录数量：",num2)



# 7.编写仿windows记事本的小程序

# 8.编写一个命令行工具，这个命令行工具就像Windows提供的cmd命令一样可以执行各种常见的命令，如dir，md, copy, move等
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    