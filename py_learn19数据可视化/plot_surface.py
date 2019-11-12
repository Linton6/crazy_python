import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

## 解决中文字体问题方法
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)

delta = 0.125
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)

X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)

Z = (Z1 - Z2) * 2
ax.plot_surface( X, Y , Z, 
                rstride = 1,
                cstride = 1,
                cmap = plt.get_cmap('rainbow'))
ax.set_zlim(-2, 2)
plt.title("3D图")
plt.show()