# -*- coding: utf-8 -*-
    #本程序需要安装BeautifulSoup库，pandas库

#导入各种需要的模块
from urllib.request import urlopen      #查找python的request模块(在标准库urllib里面)，只导入一个urlopen函数
from bs4 import BeautifulSoup           #导入BeautifulSoup库，该库通过定位HTML标签来组织复杂的网络信息

#定义存放所需信息的列表
author = []                     #构造空列表，存放“作者”
price = []                      #构造空列表，存放“价格”
book = []                       #构造空列表，存放“书名”
link = []                       #构造空列表，存放“网址”

#获取单个页面的书名，网址，价格，作者
def onePage(url):

    #生成某页面的HTML标签解析树
    html = urlopen(url)                     #打开并读取从网络获得的远程对象，即html页面
    bsObj = BeautifulSoup(html,"lxml")     #用lxml解析器对该对象html的标签进行解析，生成解析树

    #找出该页面的所有作者
    p_set = bsObj.findAll("p",{"class":"search_book_author"})   #在解析树中，找出所有的class="search_book_author"的p标签
    for p in p_set:                 #遍历p标签集合，对每个p标签进行提取
        a = p.find("a")             #提取每个p标签下的子标签中的第一个a标签
        author.append(a["title"])   #将a标签的title属性，即作者，放入author列表中

    #找出该页面的所有价格
    span_set = bsObj.findAll("span",{"class":"search_now_price"})   #在解析树中，找出所有的class="search_now_price"的span标签
    for span in span_set:           #遍历span标签集合，对每个span标签进行提取
        price.append(span.get_text())#span标签的文本内容即价格，放入price列表中

    #找出该页面的所有书名和该书的网址
    a_set = bsObj.findAll("a",{"dd_name":"单品图片"})   #在解析树中，找出所有的a标签，该标签的属性"dd_name"的属性值是"单品图片"
    for a in a_set:                 #遍历a标签集合，对每个a标签进行提取
        book.append(a["title"])     #提取a标签的属性title,即书名，放入列表book中
        link.append(a["href"])      #提取a标签的属性href,即该书网址，放入列表link中

    #检验是否每个页面的每本书都提取了四个信息，若否，则打印出的四个列表长度不一致
    print(len(book))
    print(len(link))
    print(len(author))
    print(len(price))

#构造目标链接，共5个
for num in range(1,6):
    commonLink ="http://search.dangdang.com/?key=python&act=input&page_index="      #链接的公共部分
    url =commonLink+str(num)            #链接的不同部分
    onePage(url)                        #对每个页面进行信息提取

#将四个信息列表合并为dataframe,并存到excel中
from pandas.core.frame import DataFrame
merge={"书籍":book,                      #将四个列表合并成字典
        "价格": price,
        "作者" : author,
        "网址":link}
data=DataFrame(merge)                    #将字典转换成为数据框
data.to_csv('dangdang.csv')               #将数据框存储在当前文件所在的目录下的'result.csv'中


url = "http://search.dangdang.com/?key=python&act=input&show=big&page_index="

onePage(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
fileName = 'dangdang.csv'