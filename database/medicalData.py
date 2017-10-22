from sqlalchemy import Column, Date, Integer, ForeignKey, String, Table
from dependencies import Base


class MedicalData(Base):
    __tablename__= "medical_data"
    id = Column(Integer, primary_key=True)
    alergies = Column(String(200))
    intensity = Column(String(20))
    special_condition = Column(String(50))
    blood_type = Column(String(50))
    ars = Column(String(20))
    afiliation_type = Column(String(20))
    policy_number = Column(Integer)
    student = Column(Integer, ForeignKey('students.id'))
