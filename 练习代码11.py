# =========================================290======================================
'''
from tkinter import *
import random
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.op = Label(self.master, width = 30)
        self.op['font'] = ('Courier', 20)
        self.op['bg'] = 'white'
        self.op.pack()
        bn = Button(self.master, text = "单击我")
        bn.pack()
        bn.bind('<Key>',self.one)
        # bn.bind('<Double-1>',self.double)

    def one(self,event):
        self.op['text'] = '左键单击：%s' % event.widget['text']


    def change(self):
        self.op['text'] = '欢迎学习Python'
        ct = [random.randrange(256) for x in range(3)]
        grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
        bg_color = "#%02x%02x%02x" % tuple(ct)
        self.op['bg'] = bg_color
        self.op['fg'] = 'black' if grayness > 125 else 'white'
root = Tk()
root.title("简单事件处理")
# root.geometry("250x250+30+30")
App(root)
root.mainloop()
'''

# =========================================298======================================
'''
from tkinter import *
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        text1 = Text(self.master, height = 27, width = 32)
        book = PhotoImage(file = 'G:\\08 Code\Python\\crazy_python\\timg.gif')
        text1.bm = book
        text1.insert(END, '\n')
        text1.image_create(END, image = book)
        text1.pack(side = LEFT, fill = BOTH, expand = YES)
        text2 = Text(self.master, height = 33, width = 50)
        text2.pack(side = LEFT, fill = BOTH, expand =YES)
        self.text = text2
        #创建Scroll组件
        scroll = Scrollbar(self.master, command = text2.yview)
        scroll.pack(side = RIGHT, fill = Y)
        text2.configure(yscrollcommand = scroll.set)

        text2.tag_configure('title', font=('楷体', 20, 'bold'), foreground = 'red',justify=CENTER, spacing3 = 20)
        text2.tag_configure('detail', foreground = 'darkgray', font=('微软雅黑', 11, 'bold'), \
                            spacing2 = 10, # 设置行间距
                            spacing3 = 15 # 设置段间距
                            )
        text2.insert(END, '\n')
        text2.insert(END, '疯狂Java讲义\n', 'title')
        star = PhotoImage(file = 'G:\\08 Code\Python\\crazy_python\\tqw.png')
        text2.bm = star
        details = ('更精准的搜索，更流畅的观赏；360图片收录几十亿高清美图，为用户提供壁纸、素材、'\
                     '头像、写真、摄影、风景等最新、最全的高质量图片搜索服务！\n', 
                     'Google 可能会将您在搜索时上传的图片存储7 天。这些图片不会被纳入到您的搜索记录 '+\
                     '中，并且我们仅会在该存储期间使用它们，以用于改善我们的产品和服务。\n')
        for de in details:
            text2.image_create(END, image = star)
            text2.insert(END, de, 'detail')
        url = ['https://fanyi.baidu.com/?aldtype=85#en/zh/resident','https://fanyi.baidu.com/?aldtype=85#en/zh/resident']
        name = ['京东链接', '当当链接']
        m = 0
        for each in name:
            text2.tag_configure(m, foreground = 'blue', underline = True,
                                font=('微软雅黑', 13, 'bold'))
            text2.tag_bind(m, '<Enter>',self.show_arrow_cursor)
            text2.tag_bind(m, '<Leave>',self.show_common_cursor)
            text2.tag_bind(m, '<Button-1>', self.handlerAdapter(self.click,x = url[m])) # 使用handlerAdapter包装，将当前链接参数传入到事件处理方法中
            text2.insert(END, each + '\n', m)
            m += 1
    def show_arrow_cursor(self, event):
        self.text.config(cursor='arrow')
    def show_common_cursor(self, event):
        self.text.config(cursor = 'xterm')
    def click(self, event, x):
        import webbrowser
        webbrowser.open(x)
    def handlerAdapter(self, fun , **kwds):
        return lambda event, fun = fun, kwds = kwds: fun(event,**kwds)
    
root = Tk()
root.title("text测试")
App(root)
root.mainloop()
'''

# =========================================301======================================     
'''     
from tkinter import *
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        ttk.Label(self.master, text = '选择您喜欢的图书：')\
            .pack(fill = BOTH, expand = YES)
        self.intVar = IntVar()
        books = ("疯狂Kotlin讲义", "疯狂Python讲义", 
        "疯狂Swift讲义", "疯狂java讲义")
        i = 1
        for book in books:
            ttk.Radiobutton(self.master, text = book,
                            variable = self.intVar, # 将Radiobutton绑定到self.IntVar变量
                            command = self.change, #将选中的事件绑定到self.change方法
                            value = i).pack(anchor=W)
            i += 1
        self.intVar.set(1)
    def change(self):
        from tkinter import messagebox
        messagebox.showinfo(title=None,message=self.intVar.get())
root = Tk()
root.title("Radiobutton测试")
App(root)
root.mainloop()
'''


# =========================================301======================================
'''
from tkinter import *
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个Lable组件
        ttk.Label(self.master, text = '选择你喜欢的兵种：').pack(fill = BOTH, expand=YES)
        self.intVar = IntVar()
        races = ('tqw.png','tqw.png','tqw.png')
        ranceNames = ('人族', '虫族', '神族')
        i = 1
        for rc in races:
            bm = PhotoImage(file = 'G:\\08 Code\Python\\crazy_python\\' + rc)
            r = ttk.Radiobutton(self.master, image = bm, text = ranceNames[i - 1],
                                compound = RIGHT, # 图片在文字右边
                                variable = self.intVar,#jiang 
                                command = self.change,
                                value = i
                                )
            r.bm = bm
            r.pack(anchor=W)
            i +=1
            print(self.intVar.get())
        self.intVar.set(2)
    def change(self):
        pass
root = Tk()
root.title("text测试")
App(root)
root.mainloop()
'''
# =========================================303======================================
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        ttk.Label(self.master, text = '选择你喜欢的人物：').pack(fill=BOTH, expand=YES)
        self.chars = []
        characters = {'孙悟空', '猪八戒', '唐僧', '牛魔王'}
        for ch in characters:
            intVar = IntVar()
            self.chars.append(intVar)
            cb = ttk.Checkbutton(self.master, text = ch,
                                    variable = intVar, command = self.change )
            cb.pack(anchor=W)
        ttk.Label(self.master, text = '选择你喜欢的图书：').pack(fill=BOTH, expand=YES)
        self.books = []
        books = ("疯狂Kotlin讲义", "疯狂Python讲义", 
        "疯狂Swift讲义", "疯狂java讲义")
        vals = ('Kotlin', 'Python','Swift' ,'java')
        i = 0
        for ch in vals:
            intVar = StringVar()
            self.books.append(intVar)
            cb = ttk.Checkbutton(self.master, text = ch,
                                    variable = intVar, 
                                    onvalue = vals[i],
                                    offvalue = '无',
                                    command = self.books_change )
            cb.pack(anchor=W)
            i += 1
    
    def change(self):
        new_li = [str(e.get()) for e in self.chars]
        st = ', '.join(new_li)
        messagebox.showinfo(title=None, message=st)
    def books_change(self):
        new_li = [e.get() for e in self.books]
        st = ', '.join(new_li)
        messagebox.showinfo(title=None, message=st)
root = Tk()
root.title("CheckButton测试")
# root.geometry("250x250+30+30")
App(root)
root.mainloop()

'''
# =========================================304======================================
'''
from tkinter import *
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        topF = Frame(self.master)
        topF.pack(fill=Y, expand=YES)
        self.lb = Listbox(topF)
        self.lb.pack(side=LEFT, fill=Y,expand=YES)
        for item in ['Python', 'Kotlin', 'Swift', 'Ruby']:
            self.lb.insert(END, item)
        self.lb.insert(ANCHOR, 'Python', 'Kotlin', 'Swift', 'Ruby')

        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.lb.configure(yscrollcommand=scroll.set)

        f = Frame(self.master)
        f.pack()
        Label(f, text='选择模式：').pack(side=LEFT)
        modes = ('multiple', 'browse', 'single', 'extended')
        self.strVal = StringVar()
        for m in modes:
            rb = ttk.Radiobutton(f, text = m, value = m,
                                variable = self.strVal, command = self.choose_mode)
            rb.pack(side=LEFT)
        self.strVal.set("browse")
    
    def choose_mode(self):
        print(self.strVal.get())
        self.lb['selectmode'] = self.strVal.get()

root  = Tk()
root.title("ListBox测试")
root.iconbitmap( 'G:\\08 Code\Python\\crazy_python\\key.ico')
App(root)
root.mainloop()

'''
