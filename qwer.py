# coding: utf-8
from sqlalchemy import Column, String, Integer, create_engine
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
