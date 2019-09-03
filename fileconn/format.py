
import os
def subdir_list(dirname):
    """获取目录下所有子目录名
    @param dirname: str 目录的完整路径
    @return: list(str) 所有子目录完整路径组成的列表
    """
    return list(filter(os.path.isdir,
        map(lambda filename: os.path.join(dirname, filename),
            os.listdir(dirname))))
           

def file_list(dirname, ext=".pdf"):
    """获取目录下所有特定后缀的文件
    @param dirname: str 目录的完整路径
    @param ext: str 后缀名, 以点号开头
    @return: list(str) 所有子文件名(不包含路径)组成的列表
    """
    return list(filter(
        lambda filename: os.path.splitext(filename)[1] == ext,
        os.listdir(dirname)))
       



t='/Users/cj/booksys/booktest/bookstore2'


list1=file_list(t,ext=".pdf")
