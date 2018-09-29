import datetime
from sqlalchemy import Boolean,Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship


from app import db


class User(db.Model):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)  # 字段，整形，主键 column是导入的
    name = Column(String(32))
    password = Column(String(64))
    email = Column(String(32))
    cls = Column(ForeignKey("cls.id"), nullable=True)
    phone_num = Column(String(11))
    create_time = Column(Date, default=datetime.date.today)
    auth_code = relationship("Auth_code", backref='auth_code')
    code_count = relationship("Code_count", backref='code_count')
    unit1 = relationship("Unit1", backref='unit1')
    unit2 = relationship("Unit2", backref='unit2')
    unit3 = relationship("Unit3", backref='unit3')
    unit4 = relationship("Unit4", backref='unit4')
    unit5 = relationship("Unit5", backref='unit5')
    unit6 = relationship("Unit6", backref='unit6')
    unit7 = relationship("Unit7", backref='unit7')
    unit8 = relationship("Unit8", backref='unit8')
    unit9 = relationship("Unit9", backref='unit9')

class Cls(db.Model):
    __tablename__ = 'cls'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    stu = relationship("Cls_Stu",)


class Cls_Stu(db.Model):
    __tablename__ = 'cls_stu'
    id = Column(Integer, primary_key=True)
    cls = Column(ForeignKey("cls.id"))
    name = Column(String(32))
    phone_num = Column(String(11))

class Admin_email(db.Model):
    __tablename__ = 'admin_email'
    id = Column(Integer, primary_key=True)
    email = Column(String(32))


class Code_count(db.Model):
    __tablename__ = 'code_count'  # 表名
    id = Column(Integer, primary_key=True)  # 字段，整形，主键 column是导入的
    user = Column(ForeignKey("user.id"))
    count = Column(Integer, default=0)
    data = Column(Date(), default=datetime.date.today)


class Auth_code(db.Model):
    __tablename__ = 'auth_code'
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    code = Column(String(8))


class Unit1(db.Model):
    __tablename__ = 'unit1'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))


class Unit2(db.Model):
    __tablename__ = 'unit2'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))


class Unit3(db.Model):
    __tablename__ = 'unit3'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))


class Unit4(db.Model):
    __tablename__ = 'unit4'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))


class Unit5(db.Model):
    __tablename__ = 'unit5'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))


class Unit6(db.Model):
    __tablename__ = 'unit6'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))


class Unit7(db.Model):
    __tablename__ = 'unit7'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))


class Unit8(db.Model):
    __tablename__ = 'unit8'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))


class Unit9(db.Model):
    __tablename__ = 'unit9'  # 表名
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey("user.id"))
    title = Column(String(32))
    code_counts = Column(Integer, default=0)
    exam_result = Column(String(4))
    second_exam_result = Column(String(4))
    remark = Column(String(128))
    homework = Column(String(128))