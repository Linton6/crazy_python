# 第5章
# 1、2 定义一个函数，该函数可接受一个list作为参数，该函数使用直接选择排序对list排序，或者使用冒泡排序对list排序
'''
def ss (list1):
     list1.sort()
     return list1

list1 = [3,4,2,8,34,2,6,9,12]
l = ss(list1)
print(l)

def bubble(ls): # 冒泡排序
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j+1] = ls[j + 1], ls[j]
    return ls
ls = [3,4,2,8,34,2,6,9,12]
print(bubble(ls))
'''
# 3 定义一个is_leap(year)函数，该函数可判断year是否是闰年。若是闰年，则返回true，否则返回false
'''
def is_leap(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
print(is_leap(2000))
'''
# 4 定义一个count_str_(mu_str)函数，该函数返回参数字符串中包含多少个数字、多少个英文字母，多少个空白字符，多少个其他字符
'''
def count_str_(mu_str):
    num = ['0','1','2','3','4','5','6','7','8','9']
    char = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    count_num = 0
    count_char = 0
    count_space = 0
    count_else = 0
    for i in range(len(mu_str)):
        if(mu_str[i] in num):
            count_num += 1
        elif(mu_str[i] in char):
            count_char += 1
        elif(mu_str[i] == " "):
            count_space += 1
        else:
            count_else += 1
    return count_num, count_char, count_space, count_else

strs = "123qwe rty &*()"
a,b,c,d = count_str_(strs)
print("数字个数：", a)
print("字母个数：", b)
print("空格个数：", c)
print("其他字符个数：", d)
'''

# 5 定义一个fn(n)函数，该函数返回1~n的立方和，即求1 + 2*2*2 + 3*3*3 +...+ n*n*n
'''
def fn(n):
    if n == 1:
        return 1
    return n*n*n + fn(n-1)
print(fn(4))
'''
# 6 定义一个fn(n)函数，该函数返回n的阶乘
'''
def fn(n):
    if n == 2:
        return 2
    return n * fn(n-1)
print(fn(5))
'''
# 7 定义一个函数，该函数可接受一个list作为参数，该函数用于去除list中重复的元素
'''
def fn(param):
    l = list(set(param))
    return l
ll = ["qw","qw","rt",3,45,5,3]
lq = fn(ll)
lq.sort(key = ll.index)
print(lq)
'''


# 8 定义一个fn(n)函数，该函数返回一个包含n个不重复的0-100之间整数的元组
'''
import random
def fn(n):
    ls = []
    i = 0
    while i < n:
        u = random.randint(0,10)
        if (u in ls):
            pass
        else:
            ls.append(u)
            i += 1
    return tuple(ls)
print(fn(9))
'''

# 9 定义一个fn(n)函数，其中n表示输入n行n列的矩阵（数的方阵）.在输出时，先输出n行n列矩阵，再输出该矩阵的转置形式。例如，当参数为3时，先输出：
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 再输出：
    # 1 4 7
    # 2 5 8
    # 3 6 9
def fn(n):
    for i in range(1,n+1):
        for j in range((i-1)*n +1,i*n + 1):
            print(j," ",end="")
        print()

def fn1(n):
    nn = n*n+1
    for j in range(1, n+1):
        for i in  range(j,nn,n):
            print(i," ",end="")
        print()
fn(3)
print("++++转置后++++")
fn1(3)