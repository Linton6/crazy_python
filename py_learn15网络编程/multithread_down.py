from DownUtil import *
du = DownUtil("https://static.runoob.com/images/demo/demo4.jpg", 'demo4.jpg', 3)
du.download()
def show_process():
    print("已完成： %.2f" % du.get_complete_rate())
    global t
    if du.get_complete_rate() < 1:
        # 通过定时器启动0.1秒之后执行show_process函数
        t = threading.Timer(0.1, show_process)
        t.start()
t = threading.Timer(0.1, show_process)
t.start()