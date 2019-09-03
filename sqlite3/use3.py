# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import sqlite3



    
 #   dbconn = sqlite3.connect("/Users/cj/booksys/book_DB.db")
  #  print("db connect success")
    
  #  cur = dbconn.cursor()

def dbconn(list):      
    
    for i in list[:]:
        for j in i:
      #Windows用这个  
            dbconn = sqlite3.connect("C:/booksys/book_DB.db")
            
          #Mac用这个 
          #dbconn = sqlite3.connect("/Users/cj/booksys/book_DB.db")
            
            
            
            
            cur = dbconn.cursor()
            cur.execute("INSERT INTO bookcj (id,cname,ename,author,size,format) \
            VALUES ('3', 'list[i][j]','jlist[i][j]','xxx', 33, 'list[j][i]' )")

            dbconn.commit()
            dbconn.close()

'''            
    dbconn = sqlite3.connect("/Users/cj/booksys/book_DB.db")  
    cur.execute("select * from bookcj")
    
    for item in cur.fetchall():
        for element in item:
            print(element)
            print("okkkk")
    dbconn.commit()   
    
    return 
'''




'''
CREATE TABLE "bookcj" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"cname"	TEXT NOT NULL,
	"ename"	TEXT NOT NULL,
	"author"	TEXT NOT NULL,
	"size"	INTEGER NOT NULL,
	"format"	TEXT NOT NULL
);
'''

