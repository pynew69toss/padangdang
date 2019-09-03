import requests
from bs4 import BeautifulSoup

def get_all_books():
    """
        获取该页面所有符合要求的书本的链接
    """
    url = 'http://search.dangdang.com/?key=%C9%EE%B6%C8%D1%A7%CF%B0&act=input'
    book_list = []
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    book_ul = soup.find_all('ul', {'class': 'bigimg','id':'component_0__0__6612'})
    book_ps = book_ul[0].find_all('p',{'class':'name','name':'title'})
    for book_p in book_ps:
        book_a = book_p.find('a')
        book_url = book_a.get('href')
        book_list.append(book_url)
    return book_list

#获取每本书的url，并打印出来
books = get_all_books()
for book in books:
    print(book)
