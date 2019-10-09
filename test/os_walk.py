# 作者：hao.ren3
# 时间：2019/10/8 14:44
# IDE：PyCharm

from os import walk
from os.path import exists, join

root_folder = r'C:\Users\hao.ren3\Desktop\文档'

if exists(root_folder):
    for current_folder, list_folder, list_file in walk(root_folder):
        for current_file in list_file:
            current_file_path = join(current_folder, current_file)
            if exists(current_file_path):
                print("exist ---> %s" % current_file_path)
            else:
                print("not exist ---> %s" % current_file_path)
