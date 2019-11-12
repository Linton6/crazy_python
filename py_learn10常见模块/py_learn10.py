# 第十章
# 1.提示用户输入自己的名字、年龄、身高，并将该用户信息以JSON格式保存在文件中。再写一个程序读取刚刚保存的JSON文件，恢复用户输入的信息
'''
参考网址：
https://blog.csdn.net/Jerry_1126/article/details/76409042
https://www.cnblogs.com/bigberg/p/6430095.html
# python对象转JSON对象
import json
class User:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
# def user_2_json(obj):
#     return {
#         name: obj.name
#         age: obj.age
#         height: obj.hieght
#         }
name = "Linton" # input("输入你的姓名：")
age = "25" # input("输入你的年龄：")
height = "175" # input("输入你的身高，单位cm：")
user = User(name, age, height)
f = open('user.json', 'w')
json.dump(user, f,default=lambda obj : obj.__dict__, sort_keys= False, indent=4)
# 恢复用户的输入信息
print("++++++++++")
f = open('user.json')
result = json.load(f)
print(result)
'''

# 2.给定一个字符串，该字符串只包含数字0-9、英文逗号、英文点号。请使用英文逗号、英文点号将它们分割成多个子串。
'''
# 方法一
strings = "1230,9,987.900,12,55.90"
ls = strings.replace(',','.')
print(ls)
lss = ls.split(".")
print(lss)
# 方法二
import re
strings = "1230,9,987.900,12,55.90"
strings = re.sub(',','.',strings)
ls = strings.split(".")
print(ls)
'''
# 3.定义一个正则表达式，用于验证国内的所有手机号码
'''
# 参考网址 https://blog.csdn.net/hs947463167/article/details/79463668
import re
# 验证手机号是否正确
phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
# ^ 匹配一行的开头；$匹配一行的结尾
flag = True
class User:
    def __init__(self,name):
        self.name = name
u = 1
if u:
    print("dayin")
while flag:
    phone = input('请输入您的手机号:')
    flag = False
    res = re.search(phone_pat, phone)
    print(type(res))
    print(res)
    if res:
        print('正常手机号')
    else:
        print('不是手机号')
'''
# 4.提示用户输入一个字符串，程序使用正则表达式获取该字符串中第一次重复出现的英文字母（包括大小写）
'''import re
ss ="qwerqwer"  # input("输入一个字符串：")'''



# 5.提示用户输入一个字符串和一个子串，打印出该子串在字符串中出现的 start 和end 位置；如果没有出现，则打印（-1，-1）。
# 例如用户输入：
# aaadaa
# aa
# 程序输出：
# (0, 1)
# (1, 2)
# (4, 5)
'''
import re
string ="aaadaa" # input("输入一个字符串：")
subString = "aa" # input("输入一个子串：")
# result = re.findall(subString, string)
result = re.search(subString, string)
if not result:
    print("(-1 , -1)")
else:
    i = 0
    while result:
        a = result.span(0)
        # a[1] -= 1
        print("( %d , %d)" % (a[0] + i, a[1]-1 + i))
        string = string[int(a[1] - 1):]
        i += a[1] -1
        result = re.search(subString, string)

'''


# 6.提示用户输入两行，第一行是所有学习Python的学员编号（以逗号隔开），第二行是所有学习Java的学员编号（以逗号隔开），计算所有只学Python不学Java的学员数量
'''
s1 = "100,200,300,400,500" # input("所有学习Python的学员编号（以逗号隔开）：")
s2 = "100,200,300,600,700,120" # input("所有学习Java的学员编号（以逗号隔开）")
l1 = s1.split(",")
l2 = s2.split(",")
s1 = set(l1)
s2 = set(l2)
print("只学Python不学Java的学员：")
re = s1 - s2
print(re)
print("人数",len(re))


# 7.题干与上题相同。但是要求计算既学Python又学Java的学员的数量
print("既学Python又学Java的学员：")
re = s1 & s2
print(re)
print("人数",len(re))
'''
# 8.计算用户输入的两个带时区的时间戳字符串之间相差的秒数。例如用户输入
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000    25200 / 700 = 36
# 程序应该输出：
# 25200
'''
import time
s1 = "Sun 10 May 2015 13:54:36 -0700"
s2 = "Sun 10 May 2015 13:54:36 -0000"
print(time.strptime(s1, '%a %d %b %Y %H:%M:%S %z'))
print(time.strptime(s2, '%a %d %b %Y %H:%M:%S %z'))
t1 = time.strptime(s1, '%a %d %b %Y %H:%M:%S %z')
t2 = time.strptime(s2, '%a %d %b %Y %H:%M:%S %z')
sub1 = int(s1[-5:])
sub2 = int(s2[-5:])
print(sub1,sub2)
n = 36 * (sub1 - sub2)
print(n)
print(time.mktime(t1))
print(time.mktime(t2))
print("两个时间戳相隔秒数：",abs(time.mktime(t1) - time.mktime(t2) + n))
'''

# 9.提示用户输入一个字符串，程序要输出该字符串中出现次数最多的3个字符，以及对应出现的次数。
'''
from collections import Counter
ss = input("输入一个字符串：")
c1 = Counter(ss)
ls = c1.most_common(3)
for i in ls:
    print(i)
'''

# 10.定义一个fibonacci(n)函数，该函数返回包含n个元素的斐波那契数列的列表。再使用lambda表达式定义一个平方函数，程序最终输出斐波那契数列的前n个元素的平方值

def fibonacci(n):
    ls = []
    first = 1
    second = 2
    if n == 1:
        ls.append(1)
        return ls
    if n == 2:
        ls.append(1)
        ls.append(2)
        return ls
    ls.append(1)
    ls.append(2)
    print(ls)
    for i in range(3,n+1):
        temp = first
        first = second
        second = second + temp
        # first,second = second, second+ first
        ls.append(second)
    return ls

ls = fibonacci(4)
print(ls)


