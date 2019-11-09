
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

