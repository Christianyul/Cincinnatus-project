from sqlalchemy import Column, Date, Integer, ForeignKey, String, Table
from dependencies import Base

class Course(Base):
    __tablename__="courses"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    lesson = Column(Integer)
    link = Column(String(150))
