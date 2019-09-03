# -*- coding: utf-8 -*-

import os


class readFile:
    
    def __init__(self):
        self.data = []

#遍历目录,把所有书籍名字存入列表中        
    def readpath(self,path,list):
        for root, dirs, files in os.walk(path,True):
            
            if len(files)==0:
                pass
            else:
                list.extend(files)
        return list
    
 #切割文件名和格式           
    def nametxt(self,list,blist,clist):
    
        for i in list[:]:     
            (name,txt)=os.path.splitext(i)
            blist.append(name)
            clist.append(txt)
        return blist,clist