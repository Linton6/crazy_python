# ��5��
# 1��2 ����һ���������ú����ɽ���һ��list��Ϊ�������ú���ʹ��ֱ��ѡ�������list���򣬻���ʹ��ð�������list����
'''
def ss (list1):
     list1.sort()
     return list1

list1 = [3,4,2,8,34,2,6,9,12]
l = ss(list1)
print(l)

def bubble(ls): # ð������
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j+1] = ls[j + 1], ls[j]
    return ls
ls = [3,4,2,8,34,2,6,9,12]
print(bubble(ls))
'''
# 3 ����һ��is_leap(year)�������ú������ж�year�Ƿ������ꡣ�������꣬�򷵻�true�����򷵻�false
'''
def is_leap(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
print(is_leap(2000))
'''
# 4 ����һ��count_str_(mu_str)�������ú������ز����ַ����а������ٸ����֡����ٸ�Ӣ����ĸ�����ٸ��հ��ַ������ٸ������ַ�
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
print("���ָ�����", a)
print("��ĸ������", b)
print("�ո������", c)
print("�����ַ�������", d)
'''

# 5 ����һ��fn(n)�������ú�������1~n�������ͣ�����1 + 2*2*2 + 3*3*3 +...+ n*n*n
'''
def fn(n):
    if n == 1:
        return 1
    return n*n*n + fn(n-1)
print(fn(4))
'''
# 6 ����һ��fn(n)�������ú�������n�Ľ׳�
'''
def fn(n):
    if n == 2:
        return 2
    return n * fn(n-1)
print(fn(5))
'''
# 7 ����һ���������ú����ɽ���һ��list��Ϊ�������ú�������ȥ��list���ظ���Ԫ��
'''
def fn(param):
    l = list(set(param))
    return l
ll = ["qw","qw","rt",3,45,5,3]
lq = fn(ll)
lq.sort(key = ll.index)
print(lq)
'''


# 8 ����һ��fn(n)�������ú�������һ������n�����ظ���0-100֮��������Ԫ��
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

# 9 ����һ��fn(n)����������n��ʾ����n��n�еľ������ķ���.�����ʱ�������n��n�о���������þ����ת����ʽ�����磬������Ϊ3ʱ���������
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # �������
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
print("++++ת�ú�++++")
fn1(3)