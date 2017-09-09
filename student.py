from dependencies import *
#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database
Base = declarative_base()

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
