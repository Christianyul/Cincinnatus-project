from sqlalchemy import Column, Date, Integer, ForeignKey, String, Table
from dependencies import Base
from flask_login import UserMixin
class User(Base, UserMixin):
   __tablename__ = "users"
   id= Column(Integer,primary_key=True)
   name = Column(String(50), nullable=False)
   user_name = Column(String(50))
   password = Column(String(300), nullable=False)
   email= Column(String(50), nullable=False)
   user_type= Column(String(50), nullable=False)
   student = Column(Integer, ForeignKey('students.id'))
