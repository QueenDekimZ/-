import pandas as pd
import os
from test import AddDB

def get_filename(path, filetype):
    final_name = []
    final_name_sub = []
    for root, dirs, files in os.walk(path):
        for name in files:
            for filetype_single in filetype:
                if filetype_single in name:
                    final_name.append(root + '\\' + name)
        for name in dirs:
            final_name_sub = get_filename(root + '\\' + name, filetype)
            final_name.extend(final_name_sub)
    return final_name

if __name__ == '__main__':
    path = 'F:\\Coding_Tools\\PyCharm 2018.2.4\\windmap\\各片区复核报告资料'
    filetype = ['.jpg', '.png', 'txt', 'docx']

    # 获取该文件夹下所有需要的文件路径
    final_name = get_filename(path, filetype)
    final_name_new = []
    # 清洗重复文件
    for name in final_name:
        if name not in final_name_new:
            for filetype_single in filetype:
                if filetype_single == name.split('.')[-1]:
                    print(name)
                    final_name_new.append(name)
    # print(final_name_new)

    # 实例化AddDB对象
    one = AddDB()

    for item in final_name_new:
        try:
        # 如果是docx文件将该条数据添加到数据库
            if item.split('.')[-1] == 'docx':
                # print(item)
                one.add_single_docx(path=item)
        except Exception as e:
            print("遇到错误：")
            print(e)
            # print("可能是需要筛选的文件夹下有文件打开（[Content_Types] .xml），请关闭后再运行~")
    # 关闭数据库session
    one.close_db()
