from urllib.request import *
import threading

class DownUtil:
    def __init__(self, path, target_file, thread_num):
        self.path = path
        self.thread_num = thread_num
        self.target_file = target_file
        self.threads = []
    
    def download(self):
        req = Request(url = self.path, method='GET')
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')
        f = urlopen(req)
        self.file_size = int(dict(f.headers).get('Content-Length',0))
        f.close()

        current_part_size = self.file_size
        for i in range(self.thread_num):
            start_pos = i * current_part_size
            t = open(self.target_file, 'wb') # 线程使用一个以web模式打开的文件进行下载
            t.seek(start_pos, 0)
            td = DownThread(self.path, start_pos, current_part_size, t) # 创建下载线程
            self.threads.append(td)
            td.start()
    # 获取下载完成百分比
    def get_complete_rate(self):
        sum_size = 0
        for i in range(self.thread_num):
            sum_size += self.threads[i].length
        return sum_size / self.file_size

class DownThread(threading.Thread):
    def __init__(self, path, start_pos, current_part_size, current_part):
        super().__init__()
        self.path = path
        self.start_pos = start_pos  # 当前线程下载的位置
        self.current_part_size = current_part_size
        self.current_part = current_part # 当前线程需要下载的文件块
        self.length = 0 # 定义已经下载的字节数
    
    def run(self):
        req = Request(url= self.path, method='GET')
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')
        f = urlopen(req)
        for i in range(self.start_pos):
            f.read(1)
        while self.length < self.current_part_size:
            data = f.read(1024)
            if data is None or len(data) <= 0:
                break
            self.current_part.write(data)
            self.length += len(data)
        self.current_part.close()
        f.close()

    