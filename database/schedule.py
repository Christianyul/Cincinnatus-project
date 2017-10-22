from sqlalchemy import Column, Date, Integer, ForeignKey, String, Table
from dependencies import Base


class Schedule(Base):
    __tablename__= "schedule"
    id = Column(Integer, primary_key=True)
    day = Column(String(200))
    daytime = Column(String(20))
    student = Column(Integer, ForeignKey('students.id'))
    