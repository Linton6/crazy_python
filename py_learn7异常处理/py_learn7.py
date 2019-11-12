# 第七章
# 1.提示用户输入一个N，表示用户接下来要输入N个字符串，程序尝试将用户输入的每一个字符串用空格分隔成两个整数，并计算这两个整数整除的结果。
#要求：使用异常处理机制来处理用户输入的各种错误情况，并提示用户重新输入
'''
while True:
    N = (input("输入一个字符串："))
    try:
        xy = N.split(" ")
        x = int(xy[0])
        y = int(xy[1])
        print("%d / %d : % d" % (x, y, x / y))
    except (ValueError,IndexError):
        print("输入的参数有误")
        print("重新输入：")
        continue
    except ArithmeticError:
        print("算术运算异常")
        print("重新输入：")
        continue
    except:
        print("其他异常")
        print("重新输入：")
        continue
'''

# 2.提示用户输入一个整数，如果用户输入的整数是奇数，则输出“有趣”；如果用户输入的整数是偶数，且在2-5之间，则打印“没意思”；如果用户输入的整数是偶数，且在6-20之间，
#则输出“有趣”；如果输入的整数是其他偶数，则打印“没意思”。要求：使用异常处理机制来处理用户输入的各种错误情况
'''
class NegtiveNum(Exception): pass
class PointNum(Exception): pass
try:
    N  = input("输入一个整数：")
    if  not isinstance(N,float) :
        raise PointNum("输入的是小数，请输入整数")
    N = int(N)
    if N < 0:
        raise NegtiveNum("输入的是负数，请输入整数")

    if N % 2 == 1:
        print("有趣")
    elif N == 2 or N ==4 :
        print("没意思")
    elif N % 2 == 0 and N >= 6 and N <= 20:
        print("有趣")
    else :
        print("没意思")  
except ValueError:
    print("类型错误，请输入整数")
except NegtiveNum as e:
    print(e)
except PointNum as w:
    print(w)
'''
# 3.提供一个字符元组，程序要求元组中每一个元素的长度都在5-20之间；否则程序引发异常
'''
class LengthException(Exception): pass
tuple_a = ("dsdsdds","2dsd3","1dsdsd2","fsfsfsafsdfs","fsdfds","fddsdsd")

try:
    for el in tuple_a:
        len1 = len(el)
        if len1 >= 5 and len1 <= 20:
            pass
        else:
            raise LengthException("元组的元素长度不符合要求")
    print("元组元素全部符合要求")

except LengthException as e :
    print(e)
except TypeError as e:
    print(e)
except:
    print("其他异常")
'''

# 4.提示用户输入x1，y1，x2,y2,x3,y3六个数，分别代表三个点的坐标，程序判断这个三个点是否在同一条直线上。
#要求：使用异常处理机制处理用户输入的各种错误情况，如果三个点不在同一条直线，则程序出现异常
class NotLineException(Exception):pass
try:
    x1,y1,x2,y2,x3,y3 = input("输入6个数，用空格隔开：").split()
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    y1 = int(y1)
    y2 = int(y2)
    y3 = int(y3)
    if x1 == x2 == x3 or y1== y2 == y3: # 这里做的逻辑不全面，没有考虑斜线的情况，需要做线性方程求解第三个点是否在线上
        print("三个点在同一条直线上")
    else:
        raise NotLineException("不在同一条直线上")
except NotLineException as e:
    print(e)
except ValueError:
    print("输入的参数数量不对")
