# Author:K
 2 import requests
 3 from lxml import etree
 4 from fake_useragent import UserAgent
 5 import re
 6 import csv
 7 
 8 
 9 def get_page(key):
10     for page in range(1,50):
11         url = 'http://search.dangdang.com/?key=%s&act=input&page_index=%s' % (key,page)
12         headers = {
13             'User-Agent':UserAgent().random
14         }
15         response = requests.get(url = url,headers = headers)
16         parse_page(response)
17         print('page %s over!!!' % page)
18 
19 def parse_page(response):
20     tree = etree.HTML(response.text)
21     li_list = tree.xpath('//ul[@class="bigimg"]/li')
22     # print(len(li_list))  # 测试
23     for li in li_list:
24         data = []
25         try:
26             # 获取书的标题,并添加到列表中
27             title = li.xpath('./p[@class="name"]/a/@title')[0].strip()
28             data.append(title)
29             # 获取商品链接,并添加到列表中
30             commodity_url = li.xpath('./p[@class="name"]/a/@href')[0]
31             data.append(commodity_url)
32             # 获取价格,并添加到列表中
33             price = li.xpath('./p[@class="price"]/span[1]/text()')[0]
34             data.append(price)
35             # 获取作者,并添加到列表中
36             author = ''.join(li.xpath('./p[@class="search_book_author"]/span[1]//text()')).strip()
37             data.append(author)
38             # 获取出版时间,并添加到列表中
39             time = li.xpath('./p[@class="search_book_author"]/span[2]/text()')[0]
40             pub_time = re.sub('/','',time).strip()
41             data.append(pub_time)
42             # 获取评论数,并添加到列表中
43             comment_count = li.xpath('./p[@class="search_star_line"]/a/text()')[0]
44             # 获取书本的简介,并添加到列表中.由于有些书本没有简介，所以要用try
45             commodity_detail = ''
46             commodity_detail = li.xpath('./p[@class="detail"]/text()')[0]
47             data.append(commodity_detail)
48         except:
49             pass
50         save_data(data)
51 
52 def save_data(data):
53     writer.writerow(data)
54 
55 
56 def main():
57     key = 'python'  # input('Please input key:')
58     get_page(key)
59 
60 fp = open('dangdang_Book.csv','w',encoding = 'utf-8-sig',newline = '')
61 writer = csv.writer(fp)
62 header = ['标题','链接','价格','作者','出版时间','评论数','简介']
63 writer.writerow(header)
64 main()
65 fp.close()# -*- coding: utf-8 -*-

