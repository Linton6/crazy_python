import json
from matplotlib import pyplot as plt
import numpy as np

## 解决中文字体问题方法
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

filename = r'G:\08 Code\Python\crazy_python\py_learn19数据可视化\gdp_json.json'
with open(filename) as f:
    gdp_list = json.load(f)

country_gdps = [{}, {}, {}, {}, {}]
country_codes = ['CHN', 'USA', 'JPN', 'RUS', 'CAN']
for gdp_dict in gdp_list:
    for i, country_code in enumerate(country_codes):
        # 只读取指定国家的数据
        if gdp_dict['Country Code'] == country_code:
            year = gdp_dict['Year']
            if 2017 > year > 2000:
                country_gdps[i][year] = gdp_dict['Value']
country_gdp_list = [[], [], [], [], []]
x_data = range(2001, 2017)
for i in range(len(country_gdp_list)):
    for year in x_data:
        country_gdp_list[i].append(country_gdps[i][year] / 1e8)
bar_width = 0.15
fig = plt.figure(dpi = 128, figsize=(15, 9))
colors = ['indianred', 'steelbule', 'gold', 'lightpink', 'seagreen']
countries = ['中国', '美国', '日本', '俄罗斯', '加拿大']
# 采用循环绘制5组柱状图
for i in range(len(colors)):
    plt.bar(x=np.arange(len(x_data))+bar_width*i, height=country_gdp_list[i], label=countries[i], alpha=0.8, width=bar_width)
    if i < 2:
        for x, y in enumerate(country_gdp_list[i]):
            plt.text(x, y + 100, '%.0f' % y, ha='center', va='bottom')
plt.xticks(np.arange(len(x_data))+bar_width*2, x_data)

plt.title('从2001年到2016年各国的对比')
plt.xlabel('年份')
plt.ylabel("GDP(亿美元)")
plt.legend()
plt.show()



