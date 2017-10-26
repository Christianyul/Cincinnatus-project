from sqlalchemy import Column, Date, Integer, ForeignKey, String, Table, BigInteger
from dependencies import Base


class EmergencyContact(Base):
    __tablename__="emergency_contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_mobile = Column(BigInteger, nullable=False)
    phone_home = Column(BigInteger)
    relationship = Column(String(20), nullable=False)
    student = Column(Integer, ForeignKey('students.id'))
