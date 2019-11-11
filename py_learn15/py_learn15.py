'''
from urllib.parse import *

result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)
print('scheme:',result.scheme, result[0])
print('主机和端口：',result.netloc, result[1])
print("主机：", result.params)
print("端口：",result.geturl)
'''
from urllib.request import *
result = urlopen('http://about.uuspider.com/2015/07/20/decode.html')
data = result.read()
print(data.decode('utf-8'))