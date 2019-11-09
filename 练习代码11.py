'''
from tkinter import *
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.st = StringVar()
        ttk.Entry(self.master, textvariable = self.st, width = 24, font = ('SiSong', 20, 'bold'), foreground = 'red').pack(fill = BOTH, expand = YES)
        f = Frame(self.master)
        f.pack()
        ttk.Button(f, text = '改变', command = self.change).pack(side=LEFT)
        ttk.Button(f, text='获取', command = self.get).pack(side = LEFT)
    
    def change(self):
        books = ('疯狂Python讲义', '疯狂Kotilin讲义', '疯狂Swift讲义')
        import random
        self.st.set(books[random.randint(0, 2)])
    
    def get(self):
        from tkinter import messagebox
        messagebox.showinfo(title='输入内容', message=self.st.get() )

root = Tk()
root.title("Variable的测试")
App(root)
root.mainloop()
'''

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
# =========================================306======================================
'''
from tkinter import *
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.strVar = StringVar()
        self.cb = ttk.Combobox(self.master,  textvariable=self.strVar, postcommand=self.choose)
        self.cb.pack(side=TOP)
        self.cb['values'] = ['Python', 'Ruby', 'Kotlin', 'Swift']
        f = Frame(self.master)
        f.pack()
        self.isreadonly = IntVar()
        Checkbutton(f, text = '是否只读：', variable=self.isreadonly, command=self.change).pack(side = LEFT)
    def choose(self):
        from tkinter import messagebox
        messagebox.showinfo(title=None, message=str(self.cb.get()))
    def change(self):
        self.cb['state'] = 'readonly' if self.isreadonly.get() else 'enable'
        print(self.isreadonly.get())
    def setvalue(self):
        self.strVar.set('我爱Python')
root  = Tk()
root.title("CommoBox测试")
root.iconbitmap( 'G:\\08 Code\Python\\crazy_python\\key.ico')
App(root)
root.mainloop()

'''


# =========================================317======================================
'''
from tkinter import *
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.sv = StringVar()
        self.om = ttk.OptionMenu(root,
            self.sv ,
            'Python',
            'Kotlin',
            'Ruby',
            'Swift',
            'Java',
            'Python',
            'JavaScript',
            'Erlang',
            command = self.print_option)
        self.om.pack()
        lf = ttk.LabelFrame(self.master, padding=20, text='请选择菜单方向')
        lf.pack(fill=BOTH, expand =YES,padx=10,pady=10)
        self.directions = ['below','above','left','right','flush']
        i = 0
        self.intVar = IntVar()
        for direct in self.directions:
            Radiobutton(lf, text=direct,
                        value=i,command=self.change,variable=self.intVar).pack(side=LEFT)
            i += 1
        self.intVar.set(3)

    def print_option(self, val):
        print(self.sv.get(), val)

    def change(self):
        self.om['direction'] = self.directions[self.intVar.get()]
root = Tk()
root.title("OptionMeun测试")
root.iconbitmap( 'G:\\08 Code\Python\\crazy_python\\key.ico')
App(root)
root.mainloop()

'''

# =========================================322======================================
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# 自定义对话框类，继承Toplevel
class MyDialog(Toplevel):
    def __init__(self, parent, title = None, modal=True):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        frame = Frame(self)
        self.initial_focus = self.init_widgets(frame) # ??????
        frame.pack(padx=5, pady = 5)
        self.init_buttons()
        if modal: self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        self.protocol("WM_DELETE_WINDOW", self.cancel_click)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))
        print( self.initial_focus)
        self.initial_focus.focus_set()
        self.wait_window(self)
    #通过该方法创建自定义对话框内容
    def init_widgets(self, master):
        Label(master, text='用户名', font = 12, width = 10).grid(row=1, column=0)
        self.name_entry = Entry(master, font = 16)
        self.name_entry.grid(row=1,column=1)
        Label(master, text='密 码', font = 12, width=10).grid(row=2, column=0)
        self.pass_entry = Entry(master, font = 16)
        self.pass_entry.grid(row=2, column=1)
    #通过该方法创建对话框下的按钮
    def init_buttons(self):
        f = Frame(self)
        w = Button(f, text='确定', width=10, command=self.cancel_click)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>",self.ok_click)
        self.bind("<Escape>", self.cancel_click)
        f.pack()
    def validate(self):
        return True
    def process_input(self):
        user_name = self.name_entry.get()
        user_pass = self.pass_entry.get()
        messagebox.showinfo(message='用户输入的用户名：%s,密码：%s' % (user_name, user_pass))
    def ok_click(self, event=None):
        print('确定')
        if not self.validate():
            self.initial_focus.focus_set()
            return
        self.withdraw()
        self.update_idletasks()   
        self.process_input()
        self.parent.focus_set()
        self.destroy()

    def cancel_click(self, event=None):
        print('取消')  
        self.parent.focus_set()
        self.destroy()

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        ttk.Button(self.master, text='模式对话框',command=self.open_modal).pack(side=LEFT,ipadx=5,ipady=5,padx=10)
        ttk.Button(self.master, text='非模式对话框',command=self.open_none_modal).pack(side=LEFT,ipadx=5,ipady=5,padx=10)

    def open_modal(self):
        d = MyDialog(self.master, title='模式对话框')
    def open_none_modal(self):
        d  = MyDialog(self.master, title='非模式对话框', modal=False)
root = Tk()
root.title("对话框测试")
root.iconbitmap( 'G:\\08 Code\Python\\crazy_python\\key.ico')
App(root)
root.mainloop()
'''
# ===============================330 窗口菜单===========================
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox

class App:
    def __init__(self, master):
        self.master = master
        self.init_menu()
    
    def init_menu(self):
        menubar = Menu(self.master)
        self.master.filenew_icon = PhotoImage(file = '')
        self.master.fileopen_icon = PhotoImage(file = '')
        self.master['menu'] = menubar

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='文件',menu=file_menu)

        lang_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='选择语言', menu=lang_menu)

        file_menu.add_command(label='新建', command=None, image=self.master.filenew_icon  , compound=LEFT)
        file_menu.add_command(label='打开', command=None, image=self.master.fileopen_icon  , compound=LEFT)
        file_menu.add_separator()

        sub_menu = Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label='选择性别',menu=sub_menu)
        self.genderVar = StringVar()
        for i , im in enumerate(['男', '女', '保密']):
            print(i, im)
            sub_menu.add_radiobutton(label=im, command=self.choose_gender, variable=self.genderVar, value=im)

        self.langVars = [StringVar(), StringVar(), StringVar(), StringVar()]
        for i,im in enumerate(('Python', 'Kotlin', 'Swift', 'Java')):
            print(i, im, self.langVars[i])
            lang_menu.add_checkbutton(label=im, command=self.choose_lang, onvalue = im, variable=self.langVars[i])
        
    def choose_gender(self):
        msgbox.showinfo(message=('选择的性别为：%s' % self.genderVar.get()))
    def choose_lang(self):
        rt_list = [e.get() for e in self.langVars]
        msgbox.showinfo(message=('选择的语言是：%s' % ','.join(rt_list)))

root = Tk()
root.title('菜单测试')
root.geometry('400x200')
root.resizable(width=False,height=False)
App(root)
root.mainloop()
'''

# ==============================349===================
'''
from tkinter import *

root = Tk()
cv = Canvas(root, bg = 'white')
cv.pack()
cv.create_rectangle(30, 30, 220, 150, 
                    width = 8, 
                    tags=('r1', 'r2', 'r3' ))

def first(event):
    print("第一次的函数")
def second(event):
    print("第二次的函数")

cv.tag_bind("r1", '<Button-1>', first)
cv.tag_bind('r1', '<Button-1>',second, add = True)
root.mainloop()

'''