# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 导入cv模块
# import cv2 as cv
# import numpy as np
# #第二个参数是通道数和位深的参数，有四种选择，参考https://www.cnblogs.com/goushibao/p/6671079.html
# img = cv.imread("nanjing.tif",2)
# print(img)
# #在这里一开始我写成了img.shape（），报错因为img是一个数组不是一个函数，只有函数才可以加()表示请求执行，
# #参考http://blog.csdn.net/a19990412/article/details/78283742
# print(img.shape)
# print(img.dtype)
# print(img.min())
# print(img.max())
import docx
from sqlalchemy import Column, String,Integer ,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
class Qwer(Base):
    __tablename__ = 'qwer'

    id = Column(Integer, primary_key=True)
    xmname = Column(String(100), nullable=False)
    zbx = Column(String(100), nullable=False)
    htbh = Column(String(100), nullable=False)
    lj = Column(String(100), nullable=False)
    xz = Column(String(100), nullable=False)
    pq = Column(String(100), nullable=False)
    fzr = Column(String(100), nullable=False)

class AddDB(object):
    def __init__(self):
        # 初始化数据库连接:
        engine = create_engine('mysql+mysqlconnector://root:727398239809jian@localhost:3306/wind')
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        # 创建session对象:
        self.session = DBSession()
        # path = 'F:\\Coding_Tools\\PyCharm 2018.2.4\\windmap\\各片区复核报告资料\\大客户1部\\北京市A项目\\A3小组\\赵六\\北京A项目复核报告选址.docx'

    def add_single_docx(self,path):
        print(path)
        file = docx.Document(path)
        index = 0
        zbx = ''
        group = path.split('\\')[-3]
        member = path.split('\\')[-2]
        project = path.split('\\')[-4]
        area = path.split('\\')[-5]
        for p in file.paragraphs:
            # 第一排为项目名
            # if index == 0:
            #     project = p.text
            #     index = 1
            # print(p.text)
            if '合同编号' in p.text:
                # 合同编号
                contract_no = p.text.split('：')[-1]
                # print(p.text.split('：')[-1])
            if '坐标系' in p.text:
                zbx = zbx + p.text.split('：')[-1]
            if '坐度带' in p.text:
                zbx = zbx + ',' + p.text.split('：')[-1]
            if '经纬度' in p.text:
                zbx = zbx + ',' + p.text.split('：')[-1]
        # print(group+member+area)
        # print(zbx)
        # print(path)
        # print(contract_no)
        # # 创建新User对象:
        new_user = Qwer(xmname=project,zbx=zbx,htbh=contract_no,lj=path,xz=group,pq=area,fzr=member)
        # # 添加到session:
        self.session.add(new_user)
        # # 提交即保存到数据库:
        self.session.commit()

    def close_db(self):
        # # 关闭session:
        self.session.close()

# if __name__ == '__main__':
#     path='F:\\Coding_Tools\\PyCharm 2018.2.4\\windmap\\各片区复核报告资料\\大客户1部\\北京市A项目\\A3小组\\赵六\\北京A项目复核报告选址.docx'
#     one = AddDB()
#     one.add_single(path=path)
#     one.close_db()