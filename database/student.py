from sqlalchemy import Column, Date, Integer, ForeignKey, String, Table, BigInteger
from dependencies import Base, relationship

class Student(Base):
    __tablename__="students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    image_path= Column(String(150))
    gender=Column(String(20), nullable=False)
    inscription_date = Column(Date,nullable=False)
    birthdate = Column(Date, nullable=False )
    phone_mobile = Column(BigInteger, nullable=False)
    phone_home = Column(BigInteger)
    id_document = Column(String(12))
    status = Column(String(20), nullable=False)
    ending_date = Column(Date)
    retirement_date = Column(Date)
    actual_course = Column(String(50))
    actual_lesson = Column(Integer)
    marital_status = Column(String(20))
    nationality = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)
    medical = relationship('MedicalData', cascade="all, delete-orphan")
    emergency = relationship('EmergencyContact', cascade="all, delete-orphan")
