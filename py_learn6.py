# 第六章
# 1.编写一个学生类，提供name,age,gender,phone,address,email等属性，为学生类提供带有成员变量的构造器，为学生类提供方法，用于描绘吃喝玩睡等行为

class Student:
    def __init__(self, name='Linton', age=18, gender='男', phone='110', address='中国', email='649557938@qq.com'):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email
    def eat(self,we):
        print("%d 岁的 %s 去 %s 家吃饭了" % (self.age, self.name,we))
    def drink(self):
        print("%d 岁的 %s 去喝茶了" % (self.age, self.name))
    def play(self):
        print("%d 岁的 %s 去玩了" % (self.age, self.name))
    def sleep(self):
        print("%d 岁的 %s 去睡觉了" % (self.age, self.name))
'''
student = Student("Hank",19,'男',"23123")
student.eat("Jack")
student.drink()
student.play()
student.sleep()
'''
# 2.利用第一题定义的Student类，定义一个列表保存多个Student对象作为通讯录数据。程序可通过name,email,adress查询，如果查不到数据，则进行友好提示
'''
s1 = Student(name="Linton",email="linton@qq.com",address="山东")
s2 = Student(name="Hank",email="hank@qq.com",address="江苏")
s3 = Student(name="Mary",email="mary@qq.com",address="上海")
s4 = Student(name="Bob",email="bob@qq.com",address="河南")
s5 = Student(name="Jack",email="jack@qq.com",address="山东")
list_student  = [s1, s2, s3, s4, s5]
    # 按照name查询
def queryByName(name):
    # list_name = []
    confirm = False
    for i in range(len(list_student)):
        if name in list_student[i].name:
            print("查到数据：姓名：%s 地址：%s 邮箱：%s" % (list_student[i].name, list_student[i].address, list_student[i].email))
            confirm = True
    if confirm:
        pass
    else:
        print("抱歉！没有您要查询的数据")
    # 按照email查询
def queryByEmail(email):
    # list_email = []
    confirm = False
    for i in range(len(list_student)):
        if email in list_student[i].email:
            print("查到数据：姓名：%s 地址：%s 邮箱：%s" % (list_student[i].name, list_student[i].address, list_student[i].email))
            confirm = True
    if confirm:
        pass
    else:
        print("抱歉！没有您要查询的数据")
    # 按照address查询
def queryByAddress(address):
    # list_address = []
    confirm = False
    for i in range(len(list_student)):
        if address in list_student[i].address:
            print("查到数据：姓名：%s 地址：%s 邮箱：%s" % (list_student[i].name, list_student[i].address, list_student[i].email))
            confirm = True
    if confirm:
        pass
    else:
        print("抱歉！没有您要查询的数据")

queryByName("Mary")
queryByAddress("山东")
queryByEmail("linton@qq.com")
queryByAddress("天津")
'''

# 3.定义代表二维坐标系上某个点的Point类（包括x,y两个属性），为该类提供一个方法用于计算两个Point之间的距离，再提供一个方法用于判断三个Point组成的三角形是钝角，锐角还是直角三角形
'''
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    # 判断距离
    def distance(self, a, b): # 先用实例方法，再用类方法
        x = abs(a.x - b.x)
        y = abs(a.y - b.y)
        z = x*x + y*y
        z = pow(z, 0.5)
        return z
        print("这两个点的距离：",z)
    @classmethod
    def distance_static(cls,a,b) :#使用类方法实现distance
        x = abs(a.x - b.x)
        y = abs(a.y - b.y)
        z = x*x + y*y
        z = pow(z, 0.5)
        return z
        print("这两个点的距离：",z)        
        

    # 判断三角形种类
    def judge(self, a, b,c):
        list_a = []
        list_a.append(self.distance(a,b))
        list_a.append(self.distance(c,b))
        list_a.append(self.distance(a,c))
        list_a.sort()
        if round(list_a[2] * list_a[2], 3) == round(list_a[0]*list_a[0] + list_a[1]*list_a[1], 3):
            print("三个点围起来是个直角三角形！")
        elif round(list_a[2] * list_a[2], 3) > round(list_a[0]*list_a[0] + list_a[1]*list_a[1], 3):
            print("三个点围起来是个钝角三角形！")
        else:
            print("三个点围起来是个锐角三角形！")
  
p1 = Point(3,4)
p2 = Point(3,5)
p3 = Point(5,6)
p4 = Point(5,4)
p5 = Point(2,4)
print("类方法计算两个点的距离：" ,Point.distance_static(p5,p4))
print("两个点的距离：" ,p1.distance(p5,p4))
print("两个点的距离：" ,Point.distance(p1,p4,p3))
print("两个点的距离：" ,p1.distance(p5,p3))
p1.judge(p5,p3,p1)
'''


# 4.定义代表三维笛卡尔坐标系上某个点的Point类（包括x,y,z三个属性），为该类定义一个方法，可接受b,c,d三个参数，用于计算当前点,b,c组成的面与b,c,d组成的面之间的夹角。
# 提示:cos(夹角)=(X·Y)/|X|Y|，其中X = AB * BC, Y = BC * CD,X·Y代表X与Y的点积，AB*BC代表AB和BC的叉乘。
# 知识点补充：向量的点积：a·b = a1*b1 + a2*b2 + a3 * b3 ...+an*bn ，结果是一个标量
# 知识点补充：叉乘，又叫向量积，结果是一个向量，不是标量，并且两个向量的叉乘（向量积）与这两个向量垂直  AB*BC = |AB||BC|sin<AB,BC>

# 5.定义交通工具、汽车、火车、飞机这些类，注意他们的继承关系，为这些类提供构造器

class Vehicle:
    def __init__(self, name="交通工具"):
        self.name = name
        # self.scene = scene
    def run(self):
        print(self.name,"在运行")

class Car(Vehicle):
    def __init__(self, name="汽车"):
        self.name = name
    def run(self):
        print(self.name,"在公路上跑")

class Plane(Vehicle):
    def __init__(self, name="飞机"):
        self.name = name
    def run(self):
        print(self.name,"在天上飞")

class Train(Vehicle):
    def __init__(self, name="火车"):
        self.name = name
    def run(self):
        print(self.name,"在铁轨上运行")

v = Vehicle()
v.run()
c = Car()
c.run()
p = Plane()
p.run()
t = Train()
t.run()