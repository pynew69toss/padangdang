#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
 
'''
print( os.path.basename('/root/runoob.txt') )   # 返回文件名
print( os.path.dirname('/root/runoob.txt') )    # 返回目录路径
print( os.path.split('/root/runoob.txt') )      # 分割文件名与路径
print( os.path.join('root','test','runoob.txt') )  # 将目录和文件名合成一个路径

bookpath='/Users/cj/booksys/booktest/bookstore2'

'''

bookpath='/Users/cj/booksys/booktest/bookstore2'

filename=os.path.basename(bookpath)


fileroot=os.path.dirname(bookpath)

filesplit=os.path.split(bookpath)

filejoin=os.path.join(bookpath)

print(filejoin)