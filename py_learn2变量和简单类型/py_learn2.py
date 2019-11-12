# 第二章作业
# 
# 3
"""
a = input("输入a：")
b = input("输入b：")
a = int(a)
b = int(b)
print("整除结果：",a // b)
print("带小数的除法结果：",a / b)
"""

# 4
"""
a = input("输入a：")
b = input("输入b：")
a = int(a)
b = int(b)
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
"""

# 5
'''
str1 = "ABCDCDC" # input("输入str1：")
str2 = "CDC" # input("输入str2：")
count = 0
index = 0
while index != -1 :
    index = str1.find(str2, index + 1)
    count += 1
print(count - 1)
'''

# 6
'''
a = 16
print("十进制：",a)
print("八进制：",oct(a))
print("十六进制：",hex(a))
print("二进制：",bin(a))
print("反向转换：0xff = ",int("0xff", base=16))
print("反向转换：10010010 = ",int("10010010", base=2))
'''
# 7  两种思路
msg = 'fkjava.org' # input("输入值：")
val ='6 -' # input("位置及替代字符：")
list = val.split()
a = int(list[0])
b = list[1]
re = msg[a]
table = msg.maketrans(re, b)
print(msg.translate(table))
# print(msg.replace(re,b))





