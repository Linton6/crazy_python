import csv
import pygal
from datetime import datetime
from datetime import timedelta

filename  = r'G:\08 Code\Python\crazy_python\py_learn19数据可视化\guangzhou.csv'

with open(filename) as f:
    #创建CSV读取器
    reader = csv.reader(f)
    header_row = next(reader) #读取第一行的表头数据
    print(header_row)

    shades, sunnys, cloudys, rainys = 0, 0, 0, 0
    prev_day = datetime(2016, 12, 31)
    for row in reader:
        try:
            # 将第一列的值格式化为日期
            cur_day = datetime.strptime(row[0], "%Y!%m!%d")
            description = row[3]
        except ValueError:
            print(cur_day, '数据出现错误')
        else:
            # 计算前后两天的数据时间差
            diff = cur_day - prev_day
            if diff != timedelta(days=1):
                print('%s 之前少了%d天的数据' % (cur_day, diff.days - 1))
            prev_day = cur_day
            if '阴' in description:
                shades += 1
            elif '晴' in description:
                sunnys += 1
            elif '多云' in description:
                cloudys += 1
            elif '雨' in description:
                rainys += 1
            else:
                print(description)

#创建pygal.Pie 对象（饼图）
pie = pygal.Pie()
pie.add('阴',shades)
pie.add('晴', sunnys)
pie.add('多云', cloudys)
pie.add('雨', rainys)
print(shades, sunnys, cloudys,rainys)
pie.title = '2017广州天气汇总'
pie._legend_at_bottom = True
pie.render_to_file(r'G:\08 Code\Python\crazy_python\py_learn19数据可视化\guangzhou.svg')