import matplotlib.pyplot as plt

## 解决中文字体问题方法
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

x_data = ['2011', '2012', '2013', '2014', '2015','2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data1 = [558000, 200, 6300, 7000, 84000, 9050, 10000]
plt.plot( x_data,y_data, x_data,y_data1)
plt.legend(labels=['疯狂java讲义','疯狂Python讲义'])
plt.show()