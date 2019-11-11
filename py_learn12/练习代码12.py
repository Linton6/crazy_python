

# import os
# os.symlink(r"G:\08 Code\\Python\\crazy_python\\fileopen.png", 'tt')
# os.link(r"G:\08 Code\\Python\\crazy_python\\fileopen.png",'des.jpg')

# import sys
# import re
# mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)[\.][a-z]{2,3}([\.][a-z]{2})?'
# text = sys.stdin.read()
# '''
# * p = Path('a_test.txt') # 以GBK字符集输出文本
# fsfsf@qq.com
# 2019年6月21日 - Path 对象可用于判断对应的文件是
# 否存在、是否为文件、是否为
# sdadsad@123.com
# 目录等。 ... PurePath只是代表特定平台的路径字符串，读者可
# ryrtyrty@fkiy.com
# 以把它们看做包装后的字符串（它们 .... from pathlib import 


# '''
# # sys.stdin.read()
# it = re.finditer(mailPattern, text, re.I)
# for e in it:
#     print(str(e.span()) , "--->" , e.group())


'''
import re
print (re.search('([0-9]*)x([0-9]*)','1920x1080').group())

print (re.search('([0-9]*)x([0-9]*)','1920x1080').group(0))
print (re.search('([0-9]*)x([0-9]*)','1920x1080').group(1))
print (re.search('([0-9]*)x([0-9]*)','1920x1080').group(2))
'''




'''
import sys
for lien in sys.stdin:
    print(lien,end="")
'''


'''
import fileinput
for line in fileinput.input(files=('a_test.txt', 'b_test.txt')):
    print(fileinput.filename(), fileinput.filelineno(), line, end="")
fileinput.close()
'''



'''
f = open("a_test.txt",'r',True)
while True:
    ch = f.read(1)
    if not ch :break
    print(ch, end="%")
f.close
'''



'''
import os
from pathlib import *
import time
import fnmatch
# print(os.path.abspath('.'))
# print(time.ctime())
# path = r"G:\08 Code\\Python\\crazy_python\\fileopen.png"
# print(os.path.getsize(path))
print(fnmatch.translate('?.py'))

# =========================365====================

# from pathlib import *
# # open("a_test.txt",'w')
# p = Path("a_test.txt")
# result = p.write_text('''
# 2019年6月21日 - Path 对象可用于判断对应的文件是
# 否存在、是否为文件、是否为
# 目录等。 ... PurePath只是代表特定平台的路径字符串，读者可
# 以把它们看做包装后的字符串（它们 .... from pathlib import 
# * p = Path('a_test.txt') # 以GBK字符集输出文本''', encoding='GBK')
# print(result)

# # content = p.read_text(encoding="GBK")
# # print(content)

# bb = p.read_bytes()
# print(bb)

# =========================364====================
'''
from pathlib import *
p = Path('.') 
print(p)
# for x in p.iterdir():
#     print(x)

p = Path('../')
print(p)
# for x in p.glob('**/*.py'):
#     print(x)
'''

