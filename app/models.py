import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index, Date

# 创建连接
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/go_test", encoding='utf-8', echo=True)

# 生成ORM基类
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)  # 字段，整形，主键 column是导入的
    name = Column(String(32))
    password = Column(String(64))
    create_time = Column(Date(), default=datetime.date)


class Data_Code(Base):
    __tablename__ = 'data_code'  # 表名
    id = Column(Integer, primary_key=True)  # 字段，整形，主键 column是导入的
    user = Column(ForeignKey("user.id"))
    data = Column(Date(), default=datetime.date)


class Unit1(Base):
    __tablename__ = 'unit1'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    code_counts = Column(Integer, nullable=True)
    

Base.metadata.create_all(engine)  # 在engine连接的数据库里创建表结构