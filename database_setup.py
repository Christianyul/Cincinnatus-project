from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#instancia de declarative_base

#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    name = Column(String(50), nullable=False)
    user_name = Column(String(50), primary_key=True)
    password = Column(String(50), nullable=False)
    email= Column(String(50), nullable=False)
    user_type= Column(String(50), nullable=False)

class Course(Base):
    __tablename__="courses"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)



class Student(Base):
    __tablename__="students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender=Column(String(20), nullable=False)
    inscription_date = Column(Date,nullable=False)
    birthdate = Column(Date)
    phone_mobile = Column(String(12), nullable=False)
    phone_home = Column(String(12))
    id_document = Column(String(12))
    status = Column(String(20), nullable=False)
    ending_date = Column(Date)
    retirement_date = Column(Date)
    actual_course = Column(Integer, ForeignKey('courses.id'))
    actual_lesson = Column(Integer)
    marital_status = Column(String(20), nullable=False)
    nationality = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)
    email = Column(String(50), nullable=False)

    # @property
    # #returns an object data in easily serializeable format
    # def serialize(self):
    #     return {
    #     'id': self.id
    #     'name': self.name
    #     }



class EmergencyContact(Base):
    __tablename__="emergency_contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_mobile = Column(String(12), nullable=False)
    phone_home = Column(String(12))
    relationship = Column(String(20), nullable=False)
    student = Column(Integer, ForeignKey('students.id'))


class MedicalData(Base):
    __tablename__= "medical_data"
    id = Column(Integer, primary_key=True)
    alergies = Column(String(500))
    intensity = Column(String(20))
    special_condition = Column(String(50))
    blood_type = Column(String(50))
    ars = Column(String(20))
    afiliation_type = Column(String(20))
    policy_number = Column(Integer)
    student = Column(Integer, ForeignKey('students.id'))

class Schedule(Base):
    id = Column(Integer, primary_key=True)
    day = Column(String(200))
    daytime = Column(String(20))
    student = Column(Integer, ForeignKey('students.id'))





#instance or create engine class
engine = create_engine('postgresql://scott:tiger@localhost/cincinnatus')

#this will add the classes that we will create as tables in our database
Base.metadata.create_all(engine)
