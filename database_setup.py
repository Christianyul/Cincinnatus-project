from sqlalchemy import Column,Date,Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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


    @property
    #returns an object data in easily serializeable format
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'last_name':self.last_name,
        'gender': self.gender,
        'inscription_date': self.inscription_date,
        'birthdate': self.birthdate,
        'phone_mobile': self.phone_mobile,
        'phone_home': self.phone_home,
        'id_document': self.id_document,
        'status': self.status,
        'ending_date': self.ending_date,
        'retirement_date': self.retirement_date,
        'actual_course': self.actual_course,
        'actual_lesson': self.actual_lesson,
        'marital_status': self.marital_status,
        'nationality': self.nationality,
        'address': self.address,
        'email': self.email,
        }



class EmergencyContact(Base):
    __tablename__="emergency_contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_mobile = Column(String(12), nullable=False)
    phone_home = Column(String(12))
    relationship = Column(String(20), nullable=False)
    student = Column(Integer, ForeignKey('students.id'))

    @property
    #returns an object data in easily serializeable format
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'phone_mobile': self.phone_mobile,
        'phone_home': self.phone_home,
        'relationship': self.relationship,
        'student': self.student,
        }


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

    @property
    #returns an object data in easily serializeable format
    def serialize(self):
        return {
        'id': self.id,
        'alergies': self.alergies,
        'intensity': self.intensity,
        'special_condition': self.special_condition,
        'blood_type':self.blood_type,
        'ars': self.ars,
        'afiliation_type': self.afiliation_type,
        'policy_number': policy_number,
        'student': self.student,
        }



class Schedule(Base):
    __tablename__= "schedule"
    id = Column(Integer, primary_key=True)
    day = Column(String(200))
    daytime = Column(String(20))
    student = Column(Integer, ForeignKey('students.id'))

    @property
    #returns an object data in easily serializeable format
    def serialize(self):
        return {
        'id': self.id,
        'day': self.day,
        'daytime':self.daytime,
        'student':self.student,
        }




#create database
# con = connect(user='postgres', host = 'localhost', password='0321help')
# con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cur= con.cursor()
# cur.execute('CREATE DATABASE' + " cincinnatus")
# cur.close()
# con.close()


#instance or create engine class
db_string="postgres://postgres:0321help@localhost:5432/cincinnatus"
engine = create_engine(db_string)

#this will add the classes that we will create as tables in our database
Base.metadata.create_all(engine)
