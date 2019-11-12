# 第11章
# 1. 使用Tkinter编写图形界面的计算器
'''
完成
'''
# 2. 开发并完善本章介绍的桌面弹球游戏，为桌面弹球游戏增加一些障碍物
'''
from tkinter import *
from tkinter import messagebox
import threading
import random
GAME_WIDTH = 500
GAME_HEIGHT = 680
BOARD_X = 230
BOARD_Y = 600
BOARD_WIDTH = 80
BALL_RADIUS = 9
class App:
    def __init__(self, master):
        self.master = master
        self.ball_index = 0
        self.is_lose = False
        self.curx = 260
        self.cury = 30
        self.boardx = BOARD_X  # ????为什么没放 BOARD_Y？？？
        self.init_widgets()
        self.vx = random.randint(3,6)
        self.vy = random.randint(5,10)
        self.t = threading.Timer(0.1, self.moveball)
        self.t.start()
    
    def init_widgets(self):
        self.cv = Canvas(root, background='white', width=GAME_WIDTH, height = GAME_HEIGHT)
        self.cv.pack()
        self.cv.focus_set()
        self.cv.bms = []
        for i in range(2):
            self.cv.bms.append(PhotoImage(file = 'G:\\08 Code\\Python\\crazy_python\\py_learn11\\ball' +str(i+1) + '.png'))
        
        self.ball = self.cv.create_image(self.curx, self.cury, image=self.cv.bms[self.ball_index])
        self.board = self.cv.create_rectangle(BOARD_X, BOARD_Y, BOARD_X + BOARD_WIDTH, BOARD_Y+20, width = 0, fill='lightblue')
         
        self.cv.bind('<Left>', self.move_left)
        self.cv.bind('<Right>',self.move_right)

    def move_left(self, event):
        if self.boardx <= 0:
            return
        self.boardx -= 5
        self.cv.coords(self.board, self.boardx, BOARD_Y,self.boardx+BOARD_WIDTH, BOARD_Y + 20)

    def move_right(self, event):
        if self.boardx + BOARD_WIDTH >= GAME_WIDTH:
            return
        self.boardx += 5
        self.cv.coords(self.board, self.boardx, BOARD_Y,
                        self.boardx + BOARD_WIDTH, BOARD_Y+20)
    
    def moveball(self):
        self.curx += self.vx
        self.cury += self.vy
        if self.curx + BALL_RADIUS >= GAME_WIDTH:
            self.vx = -self.vx
        if self.curx + BALL_RADIUS <= 0:
            self.vx = -self.vx
        if self.cury - BALL_RADIUS <= 0:
            self.vy = -self.vy
        if self.cury + BALL_RADIUS >= BOARD_Y: #到了挡板处
            if self.boardx <= self.curx <= (self.boardx + BOARD_WIDTH):
                self.vy = -self.vy
            else:
                messagebox.showinfo(title='失败', message='您已经输了')
                self.is_lose = True
        self.cv.coords(self.ball, self.curx, self.cury)
        self.ball_index += 1
        self.cv.itemconfig(self.ball, image=self.cv.bms[self.ball_index % 2])
        # 游戏没有失败，继续
        if not self.is_lose:
            self.t = threading.Timer(0.1, self.moveball)
            self.t.start()

root =Tk()
root.title("弹珠游戏")
root.iconbitmap('G:\\08 Code\\Python\\crazy_python\\py_learn11\\key.ico')
root.geometry('%dx%d' % (GAME_WIDTH, GAME_HEIGHT))
root.resizable(width = False, height = False)
App(root)
root.mainloop()

'''
    




# 3. 开发并完善本章介绍的五子棋游戏，为游戏增加判断输赢的功能

# 4. 开发并完善本章介绍的画图程序