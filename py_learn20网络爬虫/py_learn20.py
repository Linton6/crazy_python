'''
response.xpath('//div[@class="job-primary"]/div/h3/a/div/text()').extract()

response.css('div.job-primary>div.info-primary>h3.name span').extract()


scrapy shell https://unsplash.com/napi/photos?page=1&per_page=10&order_by=latest
'''
# 第20章
# 1.使用爬虫爬取某房产网站上广州地区的房屋出租信息，并分析广州地区出租房的热点区域。

# 2.使用爬虫自动下载http://desk.zol.com.cn/网站上的所有“风景"壁纸

# 3.整合Selenium登录crazit.org论坛，爬取该论坛“java技术”板块下的所有讨论帖子，并将数据保存到MySQL数据库中。