MY_NAME = '疯狂软件教育中心1'

def say_hi1(name):
    '''
    1定义一个打招呼的函数
    1返回对指定用户打招呼的字符串
    '''
    print("执行say_hi函数")
    return name + '您好！'

def print_rect1(height, width):
    '''
    1定义一个打印矩形的函数
    1height - 代表矩形的高
    1width - 代表矩形的宽
    '''
    print(('*' * width + '\n') * height)

class User:
    NATIONAL = 'China'
    '''
    1定义一个代表用户的类
    1该类包括name，age两个变量
    '''
    def __init__(self, name, age):
        '''
        1name初始化该用户的name
        1age初始化该用户的age
        '''
        self.name = name
        self.age = age

    def eat(self,food):
        '''
        1定义用户吃东西的方法
        1food - 代表用户正在吃的东西
        '''
        print('%s正在吃%s' % (self.name, food))