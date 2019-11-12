import matplotlib.pyplot as plt
import numpy as np

## 解决中文字体问题方法
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.figure()
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)
plt.subplot(2, 1, 1)
plt.plot(x_data, np.sin(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线')

# plt.figure()
plt.subplot(223)
plt.plot(x_data, np.cos(x_data))
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('余弦曲线')

plt.show()

