
# 构建各国GDP数据脚本
# import os
# import random
# f = open(r"G:\08 Code\Python\crazy_python\py_learn19数据可视化\data.txt",'w+')
# country_codes = ['CHN', 'USA', 'JPN', 'RUS', 'CAN']
# years = []
# for i in  range(2000,2018):
#     years.append(i) 
# print(years)
# num = 25760683041.0875
# for i in range(len(country_codes)):
#     for j in range(len(years)):
#         s = '{"Country Code": "%s" , "Country Name":"Arab World","Value": %d, "Year":%d},' % (country_codes[i], random.uniform(10,20)*num, years[j])
#         f.write(s+os.linesep)
# f.close

import datetime
s = datetime.datetime(2017, 12, 21)
print(type(s))
print(s)