# 第七章
# 1.自定义一个序列，该序列按顺序包含52张扑克牌，分别是黑桃，红心，草花，方块的2-A。要求：提供序列的各种操做方法
'''
序列相关的方法
__len__(self)
__getitem__(self, key)
__contains__(self, item)  可直接用in
__setitem__(self,item)
__delitem__(self, key)
'''
'''
def check_key(key):
    if not isinstance(key, int):raise TypeError("索引值必须是整数")
    if key < 0: raise IndexError("索引值必须是非负整数")
    if key >= 52:raise IndexError("索引值不能超过%d" % 52)

class StringCard:
    def __init__(self):
        self.__changed = {}
        self.__deleted = []

    def __len__(self):
        return 52
    
    def __getitem__(self, key):
        check_key(key)
        if key in self.__changed :
            return self.__changed[key]
        if key in self.__deleted :
            return None
        
        n = (key // 13) 
        n2 = key % 13

        list_a = ["黑桃","红心", "草花", "方块"]
        list_b = ["2","3", "4","5","6","7", "8","9","10","J", "Q","K","A"]
    
        return list_a[n] + list_b[n2]
    
    def __setitem__(self, key, value):
        check_key(key)
        self.__changed[key] = value
    
    def __delitem__(self, key):
        check_key(key)
        if key not in self.__deleted :self.__deleted.append(key)
        if key in self.__changed : del self.__changed[key]
sq = StringCard()
print(len(sq))
print(sq[5])
print(sq[1])
sq[1] = "ficnk"
print(sq[1])
del sq[1]
print(sq[1])
sq[1] = "ficdsadasnk"
print(sq[1])
print("ABC" in sq)
'''
# 2.自定义一个序列，该序列按顺序包含所有的三位数（如100，101,102，....）。要求：提供序列的各种操作方法
'''
def check_key(key):
    if not isinstance(key, int):raise TypeError("索引值必须是整数")
    if key < 0: raise IndexError("索引值必须是非负整数")
    if key >= 900:raise IndexError("索引值不能超过%d" % 900)

class SeqNum:
    def __init__(self):
        self.__changed = {}
        self.__deleted = []

    def __len__(self):
        return 900
    
    def __getitem__(self, key):
        check_key(key)
        if key in self.__changed :
            return self.__changed[key]
        if key in self.__deleted :
            return None
        
        n = 100 + key

        return n
    
    def __setitem__(self, key, value):
        check_key(key)
        self.__changed[key] = value
    
    def __delitem__(self, key):
        check_key(key)
        if key not in self.__deleted :self.__deleted.append(key)
        if key in self.__changed : del self.__changed[key]
sq = SeqNum()
print(len(sq))
print(sq[5])
print(sq[1])
sq[1] = "ficnk"
print(sq[1])
del sq[1]
print(sq[1])
sq[1] = "ficdsadasnk"
print(sq[1])
print("ABC" in sq)
'''
# 3.自定义一个迭代器，该迭代器分别返回1， 1+2， 1+2+3...的累积和
'''
class CountSum:
    # global i 
    def __init__(self, len):
        self.first = 0
        self.sec = 3
        self.__len = len
        self._i = 1
    def __next__(self):
        if self.__len == 0:
            raise StopIteration
        # 完成计算
        self.first += self._i
        self._i += 1
        # 数列长度减一
        self.__len -= 1
        return self.first
    def __iter__(self):
        return self

count = CountSum(5)
# print(next(count))
for el in count:
    print(el, end=" ")
'''
# 4.自定义一个生成器，该生成器可按顺序返回52张扑克牌，分别是黑桃，红心，草花，方块的2-A
# 生成器生成
'''
def gennerate():
    print("----------函数开始---------")
    list_a = ["黑桃","红心", "草花", "方块"]
    list_b = ["2","3", "4","5","6","7", "8","9","10","J", "Q","K","A"]   
    cur = 0
    j = 0
    # 遍历val
    for i in range(52):
        n1 = j // 13
        n2 = j % 13
        j += 1
        cur = list_a[n1] + list_b[n2]
        yield cur
g = gennerate()
print("========================")
print(next(g))
for el in g:
    print(el, end=" ")
        
'''

# 迭代器生成
'''
class CardGenerater:
    def __init__(self, len):
        self.first = 0
        self.len = len
        self.i = 0
    # def fun(self, list_a, list_b):
    #     for i in range(4):
    #         for j in range(13):
    #             return list_a[i]+list_b[j]
    def __next__(self):
        if self.len == 0:
            raise StopIteration
        list_a = ["黑桃","红心", "草花", "方块"]
        list_b = ["2","3", "4","5","6","7", "8","9","10","J", "Q","K","A"]
        
        n1 = self.i // 13
        n2 = self.i % 13
        self.first =  list_a[n1] + list_b[n2]
        self.i += 1
        self.len -= 1
        return self.first
    def __iter__(self):
        return self
count =  CardGenerater(52)
for el in count:
    print(el, end=" ")
'''

# 5.自定义一个生成器，可依次返回1,2,3,4...的阶乘
'''
def factorial(n):
        result = n
        for i in range(1,n):
                result *= i
        return result
def gennerateNum(val):
    print("--------函数开始---------")
    cur = 0
    for i in range(val):
        cur = factorial(i)
        yield cur
count =  gennerateNum(5)
for el in count:
    print(el, end=" ")
'''
# 6.自定义一个生成器，可依次访问前面目录下的所有Python源文件(以.py为后缀的文件)。
## 改成 Python读取文件夹下所有的文件
'''
import os
path = "G:\\07Blog\\Draft"#文件夹目录
files = os.listdir(path)
s = []
for file in files:
    ss =file.split(".")
    if len(ss) == 2:
        if ss[1]=="md":
            s.append(file)  
print(s)
'''
'''
import os
def QueyGenerate(path,type):
    print("-------函数开始-------")
    # path = "G:\\07Blog\\Draft"#文件夹目录
    files = os.listdir(path)
    for file in files:
        ss = file.split(".")
        if len(ss) == 2:
            if ss[1] == type:
                yield file
q = QueyGenerate("G:\\07Blog\\Draft","md")
print("=======================")
for el in q:
    print(el , end=" ")
''' 

# 7.自定义一个代表二维坐标系上某个点的Point类（包括x,y两个属性）,为Point类提供自定义的减法运算符支持，结果返回两点之间的距离
'''
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __sub__(self,other):
        if not isinstance(other, Point):
            raise TypeError("-运算符要求的目标是Point类")
        return Point(self._x - other._x,self._y - other._y)
    def __repr__(self):
        return "Point(x = %d, y = %d)" % (self._x,self._y)

p1 = Point(2,3)
p2 = Point(3,4)
p = p1 - p2
print(p)
    '''

# 8.自定义代表扑克牌的Card类（包括花色和牌面值），为Card类提供自定义的比较大小的运算符支持，大小比较标准是先比较牌面值，如果牌面值相等则比较花色，花色大小规则为：黑桃>红心>草花>方块
list_a = ["黑桃","红心", "草花", "方块"]
list_b = ["2","3", "4","5","6","7", "8","9","10","J", "Q","K","A"]
class Card:
    def __init__(self, color, num):
        self._color = color
        self._num = num
        # ==
    def __eq__(self,other):
        if not isinstance(other, Card):
            raise TypeError("==运算符要求的目标是Card类")
        if(self._color == other._color):
            if self._num == other._num:
                return True
            else:
                return False
        else:
            return False
        # >
    def __gt__(self, other):
        if not isinstance(other, Card):
            raise TypeError(">运算符要求的目标是Card类")
        if list_a.index(self._color) <= list_a.index(other._color):
            if list_a.index(self._color) == list_a.index(other._color):
                if list_b.index(self._num) <= list_b.index(other._num):
                    return False 
                else:
                    return True
            else:
                return False
        else:
            return True
        # >=
    def __ge__(self, other):
        if not isinstance(other, Card):
            raise TypeError(">=运算符要求的目标是Card类")
        if list_a.index(self._color) < list_a.index(other._color):
            return False
        else:
            if list_b.index(self._num) < list_b.index(other._num):
                return False
            else:
                return True

c1 = Card("黑桃","2")
c2 = Card("黑桃","8")
c3 = Card("红心","2")
c4 = Card("草花","2")
c5 = Card("方块","8")
c6 = Card("草花","2")
print(c1 == c2) # False
print(c1 > c2)  # False
print(c5 > c1) # True
print(c4 <= c3) # True
print(c4 == c6) # True