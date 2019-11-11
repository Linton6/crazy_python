# 第三章练习题
# 使用字典格式化字符串
'''
temp = '书名是：%(name)s, 价格是：%(price)06.2f, 出版社是:%(publish)s'
book = {'name':'疯狂Python讲义','price':89.9,'publish':'电子社'}
print(temp % book)
'''
#  1 提示用户输入N个字符串，将他们封装成元组，然后计算并输入该元组乘以3的结果，再计算并输出该元组加上('fkjava','crazyit')的结果
'''
N = input("请输入字符串个数N：")
N = int(N)
tuple1 = ()
while N > 0:
    # print(N + "")
    a = input(":")
    tuple2 = (a,)  #元组只有一个元素的时候需要加逗号
    N -= 1
    tuple1 = tuple1 + tuple2
tuple3 = tuple1 * 3 + ('fkjava','crazyit')
print(tuple3)
'''
# 2 给定一个list，将该列表的从start到end的所有元素复制到另一个list中
'''
list1 = ['ds',3,'dsd',55,'yt']
list2 = []
len1 = len(list1)
i = 0
while i < len1:
    list2.append(list1[i])
    i += 1
print(list2)
'''


# 3 用户输入一个整数n，生成长度为n的列表，将n个随机数放入列表中
'''
N = int(input("输入整数N:"))
range1 = range(N)
list = list(range1)
print(list)
'''
# 4 用户输入一个整数n，生成长度为n的列表，将n个随机的奇数放入列表中
'''
N = int(input("输入整数N:"))
list = []
N = 2 * N
i = 1
while  N > i:
    list.append(i)
    i += 2
print(list)
'''

# 5 用户输入一个整数n，生成长度为n的列表，将n个随机的大写字符放入列表中
'''
import random
N = int(input("输入整数N:"))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet.upper()
list = []
i = 0
while  N > i:
    char = random.choice(alphabet)
    list.append(char)
    i += 1
print(list)
'''
# 6 用户输入N个字符串，将这些字符串收集到列表中，然后去除其中重复的字符串后输出列表
'''
N = int(input("输入整数N:"))
list1 = []
i= 0
while N > i:
    # print("第 %d 个字符串：" % i) 
    i += 1
    msg =  input("第 %d 个字符串：" % i )
    list1.append(msg)
print(list(set(list1)))  # 元素的排序会改变

l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)  # 保持元素顺序不变
'''
# 7 用户输入以空格分隔的多个整数，程序将这些整数转换为元组元素，并输出该元组及其hash值（使用内置的hash函数）
'''
strs = '10 20 30 40 50' # input("以空格分隔的多个整数:")
strs = strs.replace(" ", ',')
print(strs)
# 列表，元组和字符串，他们之间的互相转换使用三个函数，str(),tuple()和list()
arr = '10 20 30 40 50' #  input("")
num = [int(n) for n in arr.split()]
tuple1 = tuple(num)
print(tuple1)
print(type(tuple1))
print(hash(tuple1))
'''
# 8 用户随机输入N个大写字母，程序使用dict统计用户输入的每个字母的次数
msg = "h h h J K L Y Y Y U I" # input("随机输入N个大写字母：")
list1  = msg.split()
len1 = len(list1)
dict1 = {}
i = 0
while len1 > i:
    if list1[i] in dict1:
        num = dict1[list1[i]]
        num += 1
        dict1[list1[i]] = num
    else:
        dict1[list1[i]] = 1
    # num = int(dict1.setdefault(list1[i], int(1)))
    # if(num != 1):
    #     num += 1
    #     dict1[list1[i]] = num
    i += 1
print(dict1)




